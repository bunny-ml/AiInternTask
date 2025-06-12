import requests
from backend.app.config.config import GROQ_API_KEY

def ask_llm(context , question):
    url = "https://api.groq.com/openai/v1/chat/completions"
    api_key = GROQ_API_KEY

    header={
        "Authentication": f"Bearer{api_key}",
        "content-Type": "application/json"
    }

    body = {
        "model": "llama3-70b-8192",
        "meassages":[
            {"role": "syetem" , "content": "You are AI assistant. Use the context to answer claerly and also give theme of the document."},
            {"role": "user" , "content": f"Content: {content}\n\nQuestion: {question}"}   
            ],
            "temperature": 0.3
    }

    response = requests.post(url, json= body , headers= header)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return F"Error:{response.text}"