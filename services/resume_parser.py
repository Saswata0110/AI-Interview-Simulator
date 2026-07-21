import fitz  # PyMuPDF


class ResumeParser:

    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_text(self):

        try:

            document = fitz.open(self.pdf_path)

            text = ""

            for page in document:
                text += page.get_text()

            document.close()

            return text.strip()

        except Exception as e:

            print("Resume Parsing Error:", e)

            return None