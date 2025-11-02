from google import genai
import os

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def ask_gemini(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
