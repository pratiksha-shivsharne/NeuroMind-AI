from pypdf import PdfReader


def extract_text_from_pdf(pdf_file):
    """
    Reads a PDF file and returns all extracted text.
    """

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    return text