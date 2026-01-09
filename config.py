import os
import google.generativeai as genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("❌ GEMINI_API_KEY not set")

genai.configure(api_key=GEMINI_API_KEY)

MODEL = genai.GenerativeModel("gemini-2.5-flash")
