# 🌟 Gemini Chatbot CLI

## 🚀 Project Purpose

An interactive Command Line Interface chatbot powered by Google's Gemini API. Built to demonstrate rapid deployment of LLM-based assistants and lay the foundation for integration into larger AI products like **SmartHire AI**.

## ⚙️ Setup

### 1\. Clone repository

bash

CopyEdit

`git clone YOUR_REPO_URL cd gemini-chatbot`

### 2\. Create virtual environment

bash

CopyEdit

`python3 -m venv myenv source myenv/bin/activate`

### 3\. Install dependencies

bash

CopyEdit

`pip install -r requirements.txt`

### 4\. Create `.env` with your Gemini API key

ini

CopyEdit

`GEMINI_API_KEY=YOUR_API_KEY_HERE`

## 💻 Usage

Run the chatbot:

bash

CopyEdit

`python3 chatbot_gemini.py`

Type messages to receive real-time Gemini responses.

## ✨ Features

✅ Gemini API integration  
✅ Environment variable security via python-dotenv  
✅ Clean CLI interface for rapid prototyping

## 🔮 Future Enhancements

*   LangChain integration for advanced pipelines
    
*   Conversation memory to hold context between turns
    
*   FastAPI/Flask routes for backend integration
    
*   Integration into SmartHire AI for resume and job flow chats
    
*   Local model deployment for cost-free operation (e.g. Ollama, Mistral)
    

## 🧑‍💻 Author

Built by **\[Your Name\]** as part of an AI engineering learning journey and the upcoming **SmartHire AI** project suite.

* * *

## ✅ requirements.txt (full)

Your current environment’s **minimal requirements.txt** for this project:

text

CopyEdit

`google-generativeai==0.8.5 python-dotenv==1.1.1`

If you prefer to lock all packages in your environment, run:

bash

CopyEdit

`pip freeze > requirements.txt`

But to keep it clean for this CLI-only project, the minimal above is sufficient.