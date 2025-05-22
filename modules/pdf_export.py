from xhtml2pdf import pisa
from io import BytesIO

def convert_html_to_pdf(source_html):
    result = BytesIO()
    pisa_status = pisa.CreatePDF(source_html, dest=result)
    return result if not pisa_status.err else None
