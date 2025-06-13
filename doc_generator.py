# utils/doc_generator.py

from docx import Document
import os

TEMPLATE_PATH = "templates/SLI_template.docx"
OUTPUT_FOLDER = "generated_surat"

def generate_sli_letter(nama, nokp, no_pelajar, program, tarikh_surat):
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    doc = Document(TEMPLATE_PATH)

    # Gantikan placeholder dalam template
    for p in doc.paragraphs:
        if "«NAMA_PENUH_HURUF_BESAR»" in p.text:
            p.text = p.text.replace("«NAMA_PENUH_HURUF_BESAR»", nama.upper())
        if "«NOMBOR_KAD_PENGENALAN»" in p.text:
            p.text = p.text.replace("«NOMBOR_KAD_PENGENALAN»", nokp)
        if "«NOMBOR_ID_PELAJAR»" in p.text:
            p.text = p.text.replace("«NOMBOR_ID_PELAJAR»", no_pelajar)
        if "«NAMA_PROGRAM»" in p.text:
            p.text = p.text.replace("«NAMA_PROGRAM»", program)
        if "«TARIKH_SURAT»" in p.text:
            p.text = p.text.replace("«TARIKH_SURAT»", tarikh_surat)

    filename = f"SLI_{no_pelajar}.docx"
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    doc.save(filepath)
    return filepath
