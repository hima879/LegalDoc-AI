from fastapi import FastAPI

app = FastAPI()

@app.get("/summarize")
def summarize_demo():
    return {"simplified_text": "This is a placeholder for the AI simplified output."}

