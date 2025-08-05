import streamlit as st
import cv2
import numpy as np
from PIL import Image
import pytesseract
from ultralytics import YOLO
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="📷 Camera Mode - Gemini Vision", layout="centered")
st.title("🎯 VisuaLens - Live Object & Text Insight (Gemini)")

run = st.checkbox("🎥 Start Camera")
FRAME_WINDOW = st.image([])

# Load YOLO model
model_yolo = YOLO("yolov8n.pt")  # you can change to yolov8s.pt or yolov8m.pt

if run:
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        st.error("❌ Cannot open webcam.")
    else:
        while run:
            ret, frame = cap.read()
            if not ret:
                st.warning("⚠️ Failed to read frame.")
                break

            results = model_yolo.predict(frame, conf=0.4, verbose=False)
            annotated_frame = results[0].plot()

            descriptions = []
            for box in results[0].boxes:
                cls = int(box.cls[0])
                label = results[0].names[cls]

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                roi = frame[y1:y2, x1:x2]

                roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
                roi_pil = Image.fromarray(roi_rgb)

                text = pytesseract.image_to_string(roi_pil).strip()
                descriptions.append((label, text, roi_pil))

            img_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
            FRAME_WINDOW.image(img_rgb)

            if descriptions:
                st.markdown("### 🧠 Detected & Extracted")
                for label, text, image_pil in descriptions:
                    st.markdown(f"**🧾 {label.upper()}**")
                    st.image(image_pil, width=300, caption="Detected ROI")

                    if text:
                        st.markdown(f"`📝 OCR:` {text[:100]}")

                    if st.button(f"🤖 Ask Gemini about this", key=label + text[:8]):
                        with st.spinner("Gemini is thinking..."):
                            response = model.generate_content(
                                f"Explain this object labeled '{label}' that contains the text: {text}"
                            )
                            st.success(response.text)

        cap.release()
