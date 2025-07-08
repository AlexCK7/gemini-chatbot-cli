from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure with your API key from .env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use a valid available model, for example:
model_name = "models/gemini-1.5-flash"

model = genai.GenerativeModel(model_name)

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    response = model.generate_content(user_input)
    print("Gemini:", response.text)
