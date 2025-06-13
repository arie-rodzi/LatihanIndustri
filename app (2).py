
import streamlit as st
from docx import Document
from datetime import date
import os

TEMPLATES_DIR = "templates"

def generate_doc(template_name, data, output_name):
    doc = Document(os.path.join(TEMPLATES_DIR, template_name))
    for para in doc.paragraphs:
        for key, val in data.items():
            para.text = para.text.replace(f"«{key}»", val)
    output_path = f"{output_name}.docx"
    doc.save(output_path)
    return output_path

def form_bli02():
    st.subheader("BLI-02: Jawapan Latihan Industri dari Organisasi")
    with st.form("form_bli02"):
        nama_pelajar = st.text_input("Nama Pelajar")
        program = st.text_input("Program")
        nama_syarikat = st.text_input("Nama Syarikat")
        alamat_syarikat = st.text_area("Alamat Syarikat")
        nama_pegawai = st.text_input("Nama Pegawai")
        jawatan_pegawai = st.text_input("Jawatan Pegawai")
        telefon_pegawai = st.text_input("Telefon Pegawai")
        email_pegawai = st.text_input("Email Pegawai")
        elaun = st.text_input("Elaun")
        tarikh = st.date_input("Tarikh", value=date.today())
        submit = st.form_submit_button("Hasilkan BLI-02")
        if submit:
            data = {
                "NAMA_PELAJAR": nama_pelajar,
                "PROGRAM": program,
                "NAMA_SYARIKAT": nama_syarikat,
                "ALAMAT_SYARIKAT": alamat_syarikat,
                "NAMA_PEGAWAI": nama_pegawai,
                "JAWATAN_PEGAWAI": jawatan_pegawai,
                "TELEFON_PEGAWAI": telefon_pegawai,
                "EMAIL_PEGAWAI": email_pegawai,
                "ELAUN": elaun,
                "TARIKH": tarikh.strftime("%d %B %Y")
            }
            filepath = generate_doc("borang_jawapan.docx", data, "BLI02_" + nama_pelajar.replace(" ", "_"))
            with open(filepath, "rb") as file:
                st.download_button("📥 Muat Turun BLI-02", file, file.name)

def form_bli03():
    st.subheader("BLI-03: Pengesahan Penempatan")
    with st.form("form_bli03"):
        nama_pelajar = st.text_input("Nama Pelajar")
        no_pelajar = st.text_input("No Pelajar")
        no_ic = st.text_input("No Kad Pengenalan")
        nama_syarikat = st.text_input("Nama Syarikat")
        alamat_syarikat = st.text_area("Alamat Syarikat")
        tarikh = st.date_input("Tarikh Pengesahan", value=date.today())
        submit = st.form_submit_button("Hasilkan BLI-03")
        if submit:
            data = {
                "NAMA_PELAJAR": nama_pelajar,
                "NO_PELAJAR": no_pelajar,
                "NO_KAD_PENGENALAN": no_ic,
                "NAMA_SYARIKAT": nama_syarikat,
                "ALAMAT_SYARIKAT": alamat_syarikat,
                "TARIKH": tarikh.strftime("%d %B %Y")
            }
            filepath = generate_doc("borang_pengesahan.docx", data, "BLI03_" + nama_pelajar.replace(" ", "_"))
            with open(filepath, "rb") as file:
                st.download_button("📥 Muat Turun BLI-03", file, file.name)

def form_bli04():
    st.subheader("BLI-04: Lapor Diri")
    with st.form("form_bli04"):
        nama_pelajar = st.text_input("Nama Pelajar")
        no_ic = st.text_input("No Kad Pengenalan")
        no_pelajar = st.text_input("No Pelajar")
        program = st.text_input("Program")
        nama_syarikat = st.text_input("Nama Organisasi")
        alamat_syarikat = st.text_area("Alamat Organisasi")
        tarikh_lapor = st.date_input("Tarikh Lapor", value=date.today())
        submit = st.form_submit_button("Hasilkan BLI-04")
        if submit:
            data = {
                "NAMA_PELAJAR": nama_pelajar,
                "NO_KAD_PENGENALAN": no_ic,
                "NO_PELAJAR": no_pelajar,
                "PROGRAM": program,
                "NAMA_SYARIKAT": nama_syarikat,
                "ALAMAT_SYARIKAT": alamat_syarikat,
                "TARIKH": tarikh_lapor.strftime("%d %B %Y")
            }
            filepath = generate_doc("borang_lapor_diri.docx", data, "BLI04_" + nama_pelajar.replace(" ", "_"))
            with open(filepath, "rb") as file:
                st.download_button("📥 Muat Turun BLI-04", file, file.name)

st.title("📄 Sistem Pengurusan Latihan Industri UiTM NS")
tab = st.sidebar.radio("Pilih Borang", ["BLI-02", "BLI-03", "BLI-04"])

if tab == "BLI-02":
    form_bli02()
elif tab == "BLI-03":
    form_bli03()
elif tab == "BLI-04":
    form_bli04()
