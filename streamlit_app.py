


import streamlit as st
import requests

# ✅ Replace with your actual Flask URL
FLASK_URL = "https://5000-bunnyml-aiinterntask-b42ekyib5rj.ws-us120.gitpod.io/"

st.set_page_config(page_title="DocChat", layout="centered")
st.title("📚 DocChat: Ask Questions About Your Document")

# 🔁 Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "context" not in st.session_state:
    st.session_state.context = ""

# 📤 File uploader
uploaded_file = st.file_uploader("Upload a PDF or image", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file:
    with st.spinner("Extracting text from the file..."):
        files = {"file": uploaded_file}
        res = requests.post(f"{FLASK_URL}/upload", files=files)

        if res.status_code == 200:
            st.session_state.context = res.json().get("text", "")
            st.success("Text extracted successfully!")
        else:
            st.error("Failed to extract text from document.")

# 💬 Chat Interface
if st.session_state.context:
    st.subheader("Chat with your document")

    # ✅ Text input instead of st.chat_input
    question = st.text_input("Type your question here:")
    send_btn = st.button("Send")

    if send_btn and question.strip():
        with st.spinner("Asking your question..."):
            payload = {
                "question": question,
                "context": st.session_state.context
            }
            res = requests.post(f"{FLASK_URL}/ask", json=payload)

            if res.status_code == 200:
                answer = res.json().get("answer", "No answer returned.")
                st.session_state.chat_history.append(("🧑‍💻 You", question))
                st.session_state.chat_history.append(("🤖 Bot", answer))
            else:
                st.error("Error getting a response from the backend.")

    # 💬 Display the full chat history
    for speaker, msg in st.session_state.chat_history:
        st.markdown(f"**{speaker}:** {msg}")

