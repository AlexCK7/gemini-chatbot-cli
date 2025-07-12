# 🌟 Gemini Chatbot CLI

## 🚀 Project Purpose

An interactive Command Line Interface chatbot powered by Google's Gemini API. Built to demonstrate rapid deployment of LLM-based assistants and lay the foundation for integration into larger AI products like **SmartHire AI**.

## ⚙️ Setup

### 1\. Clone repository

```bash
git clone https://github.com/AlexCK7/gemini-chatbot-cli.git
cd gemini-chatbot-cli
```

### 2\. Create virtual environment

```bash
python3 -m venv myenv source myenv/bin/activate
```

### 3\. Install dependencies

```bash
pip install -r requirements.txt
```

### 4\. Create `.env` file

Create a `.env` file in the project root and add your Gemini API key:

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

* * *

## 💻 Usage

### ▶️ CLI Mode

Run the chatbot interactively from your terminal:

```bash
python3 chatbot_gemini.py
```

Type your messages and receive real-time Gemini responses.

* * *

### 🛰️ API Access (Optional)

You can also run the chatbot as a FastAPI server:

```bash
uvicorn app:app --reload
```

Then send a POST request to `/chat` with a JSON body containing a `message` key:

**Example:**

```bash
curl -X POST http://127.0.0.1:8000/chat \      
-H "Content-Type: application/json" \      
-d '{"message": "Tell me a joke"}'
```

* * *

## ✅ requirements.txt (full)

This project requires the following minimal dependencies:

```text
google-generativeai==0.8.5 
python-dotenv==1.1.1 
fastapi==0.111.0 
uvicorn==0.30.1 
pydantic==2.7.1
```

If you prefer to lock all packages to your current environment:

```bash
pip freeze > requirements.txt
```

* * *

## 🧪 Terminal Setup (if terminal was reset)

If your terminal session was closed or reset:

 1.  **Open a terminal**
     
 2.  Navigate back into the project:    

```bash
cd ~/Desktop/gemini-chatbot-cli
```

3.  Reactivate your environment:

```bash
source myenv/bin/activate
```

4.  Reinstall packages (if needed):

```bash
pip install -r requirements.txt
```

* * *

## ✨ Features

✅ Gemini API integration  
✅ FastAPI server mode for API-based usage  
✅ Environment variable security via `python-dotenv`  
✅ Clean CLI interface for rapid prototyping  
✅ Easy local deployment and expansion

* * *

## 🔮 Future Enhancements

* *   🔗 LangChain integration for advanced multi-step pipelines
*     
* *   🧠 Add memory to retain conversation history
*     
* *   🧩 Seamless SmartHire AI integration
*     
* *   💡 Deploy with Ollama or Mistral (local open-source LLMs)
*     
* *   📦 Containerize with Docker for production-ready use  

* * *

## 📁 Project Structure

```text
gemini-chatbot-cli/
├── app.py                 # FastAPI server entry point
├── chatbot_gemini.py      # CLI chatbot interface
├── requirements.txt       # Dependencies
├── .env                   # Your Gemini API key (NOT committed)
├── .gitignore             # Hides .env and venv
└── README.md              # Project overview and instructions
```

* * *

## 🧑‍💻 Author

Built by **TAIGA** as part of an AI engineering learning journey and the upcoming **SmartHire AI** product suite.  
Always evolving. Always shipping.