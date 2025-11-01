from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)  # allows frontend to access backend

# Configure Gemini API
genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")

model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        question = data.get("question", "")
        if not question:
            return jsonify({"answer": "Please enter a question."})
        
        response = model.generate_content(question)
        return jsonify({"answer": response.text})
    except Exception as e:
        return jsonify({"answer": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)

