import json
import os

def load_groq_config():
    config_path = os.path.join(os.path.dirname(__file__),"api_key.json")
    with open(config_path, "r") as f:
        data = json.load(f)
    return data.get("GROQ_API_KEY")

GROQ_API_KEY = load_groq_config()