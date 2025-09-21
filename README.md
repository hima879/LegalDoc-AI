# LegalDoc-AI
AI Legal Document Simplifier
A Generative AI tool that transforms complex legal documents into easy-to-understand guidance.

# Problem Statement
Legal documents like rental agreements, loan contracts, and terms of service are filled with complex jargon that is difficult for ordinary users to understand. This creates information asymmetry and legal risks.

# Objective
Develop a generative AI solution that provides simplified summaries, clause explanations, and interactive Q&A in text and voice formats while ensuring privacy.

# Our Approach
1. Document Upload: Accept PDF/DOCX/Image.
2. Text Extraction: Use pdfplumber, docx2txt, Tesseract OCR.
3. Summarization: flan-t5-large / legal-summarizer-bart.
4. Refinement for Voice: Gemini LLM converts text to conversational style.
5. Q&A Layer: all-MiniLM-L6-v2 embeddings + FLAN-T5-small for clause-specific answers.
6. Voice Output: Coqui TTS.
7. Privacy: Presidio masks PII.

# Unique Selling Proposition (USP)
- Multilingual Support via Gemini.
- Complete pipeline: Upload → Simplify → Ask → Listen.
- Privacy-first design: local models + controlled Gemini usage.

# Features
- Document upload and parsing
- Legal text simplification
- Summarization of key clauses
- Interactive Q&A
- Voice-enabled output
- Privacy protection (PII masking)

# Tech Stack
- Backend: Python, FastAPI / Flask
- Frontend: Streamlit
- Models: flan-t5-large, legal-summarizer-bart, FLAN-T5-small, Gemini LLM, all-MiniLM-L6-v2
- Text Extraction: pdfplumber, docx2txt, Tesseract OCR
- Text-to-Speech: Coqui TTS
- Privacy & Security: Presidio
- Database (RAG): FAISS / ChromaDB
