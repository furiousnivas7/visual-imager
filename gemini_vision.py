import google.generativeai as genai
from dotenv import load_dotenv
import os
from PIL import Image

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")  # ✅ Spelling corrected

def describe_image(pil_image, prompt="Describe this image in detail."):
    response = model.generate_content(
        [prompt, pil_image],
        stream=False,
    )
    description = response.text

    # Only extract keywords if it's the default prompt
    if prompt == "Describe this image in detail.":
        keyword_response = model.generate_content(
            [f"Extract 5 to 10 important keywords from this description:\n{description}"]
        )
        keywords = keyword_response.text.split(",")
        keywords = [kw.strip() for kw in keywords if kw.strip()]
        return description, keywords
    else:
        return description

