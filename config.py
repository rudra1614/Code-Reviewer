import google.generativeai as genai

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

genai.configure(api_key=GEMINI_API_KEY)

MODEL = genai.GenerativeModel("gemini-1.5-flash")
