
import streamlit as st
from pypdf import PdfReader
from io import BytesIO

st.set_page_config(
    page_title="DocuMind AI",
    page_icon="📚"
)

st.title("📚 DocuMind AI")
st.write("Upload a PDF and explore its contents.")

uploaded_file = st.file_uploader(
    "Choose a PDF document",
    type=["pdf"]
)

if uploaded_file:
    reader = PdfReader(BytesIO(uploaded_file.getvalue()))

    pages = [
        page.extract_text() or ""
        for page in reader.pages
    ]

    st.success(f"PDF loaded! Total pages: {len(pages)}")

    keyword = st.text_input("Search your document")

    if keyword:
        matches = [
            (i + 1, text)
            for i, text in enumerate(pages)
            if keyword.lower() in text.lower()
        ]

        if matches:
            for page_number, text in matches:
                with st.expander(f"Page {page_number}"):
                    st.write(text[:3000])
        else:
            st.info("No matching text found.")

    with st.expander("Preview extracted text"):
        st.text("\n\n".join(pages)[:5000])
else:
    st.info("Upload a PDF to get started.")
