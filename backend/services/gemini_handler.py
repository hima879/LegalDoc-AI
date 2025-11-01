import google.generativeai as genai
import os

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def ask_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

