import pytesseract
from PIL import Image # for images
import fitz # PyMuPDF
import io 


def extract_text_from_file(file):
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file)
    else:
        return extract_text_from_image(file)

def extract_text_from_image(file):
    image = Image.open(file)
    text = pytesseract.image_to_string(image)

    return text

def extract_text_from_pdf(file):
    text =""
    pdf_bytes = file.read()
    pdf = fitz.open(stream=pdf_bytes , filetype="pdf")

    for page in pdf:
        pix = page.get_pizmap()
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        text += pytesseract.image_to_string(img)


    return text
