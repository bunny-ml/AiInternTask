from flask import Blueprint , request , jsonify , render_template
from backend.app.utils.ocr_engine import extract_text_from_file
from backend.app.services.chat_llm import ask_llm


api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("/")
def home():
    return "flask is runnig on streamlit"

@api_blueprint.route("/upload" , methods= ["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error":"NO file uploads"}), 400

    file = request.files['file']
    text = extract_text_from_file(file)

    return jsonify({"text":text})


@api_blueprint.route("/ask" , methods=["POST"])
def ask_question():
    data = request.json
    question = data.get("question")
    context = data.get("context")

    if not question or not context:
        return jsonify({"error":"Missing question or context"}) , 400

    answer = ask_llm(context, question)

    return jsonify({"answer": answer})
    