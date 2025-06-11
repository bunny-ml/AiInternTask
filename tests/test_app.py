import requests

# Upload a scanned image or PDF
file_path = "backend/data/sample.png"  

upload_response = requests.post(
    "http://localhost:5000/api/upload",
    files={"file": open(file_path, "rb")}
)

extracted_text = upload_response.json().get("text")
print("\n📝 Extracted Text:\n", extracted_text)

# Ask a question based on the extracted text
question = "What is the theme?"

ask_response = requests.post(
    "http://localhost:5000/api/ask",
    json={"context": extracted_text, "question": question}
)

print("\n💬 Answer from LLM:\n", ask_response.json().get("answer"))
