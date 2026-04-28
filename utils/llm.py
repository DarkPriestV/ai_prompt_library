import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",   # ✅ THIS ONE WORKS
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"