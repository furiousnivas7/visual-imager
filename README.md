# 📸 visual-imager

**AI-Powered Visual Search Engine**  
Detect, extract, and understand the world through your camera or uploaded images.

---

## 🚀 Overview

**visual-imager** is a real-time visual search application that allows users to:
- Upload an image or use their webcam
- Detect objects using YOLO (Ultralytics)
- Extract text using OCR (Tesseract)
- Use **Google Gemini API** to interpret and search content intelligently

Whether it’s a product, a place, or a phrase in an image, this tool empowers AI-driven image understanding in seconds.

---

## ✨ Features

- 📷 **Dual Input Modes**: Upload an image or use live camera feed
- 🧠 **YOLO Object Detection**: Identify multiple objects in real time
- 🔍 **Text Recognition (OCR)**: Extract printed or handwritten text
- 🤖 **Gemini-Powered Search**: Smart search suggestions and contextual understanding
- 🖥️ **Streamlit Interface**: Simple, responsive, and fast UI

---

## 🛠 Tech Stack

| Layer      | Tools Used                                   |
|------------|----------------------------------------------|
| Frontend   | Streamlit                                     |
| Backend    | Python, OpenCV, Tesseract OCR, Ultralytics YOLO |
| AI Engine  | Google Gemini API                             |
| Extras     | dotenv, PIL, NumPy, Requests, etc.            |

---

## 🧪 Installation

1. **Clone the repository**  
```bash
git clone https://github.com/furiousnivas7/visual-imager.git
cd visual-imager
#Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
#Install dependencies
pip install -r requirements.txt
#Set up your API key
#Create a .env file in the root directory and add:
GEMINI_API_KEY=your_google_gemini_api_key
#▶️ Running the App
streamlit run app.py
#The app will open in your browser at http://localhost:8501.