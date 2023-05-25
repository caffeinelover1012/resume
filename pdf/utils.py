import PyPDF2
import re

def pypdfExtract(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file, strict=False)
    pdf_text = []

    for page in reader.pages:
        content = page.extract_text()
        pdf_text.append(content)

    return pdf_text
