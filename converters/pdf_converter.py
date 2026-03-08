import pdfplumber


def convert_pdf(file_path):
    pages = []

    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()

            pages.append({
                "page": i + 1,
                "text": text
            })

    return {
        "type": "pdf",
        "pages": len(pages),
        "content": pages
    }