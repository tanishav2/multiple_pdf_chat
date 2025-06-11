import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks




def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multple PDFs", page_icon=":books:")
    st.header("Chat with multiple PDFs :books:")
    st.text_input ("Ask a questions about your documents:")

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload PDF files and click on Process", type=["pdf"], accept_multiple_files=True)
        process_button = st.button("Process")
        if process_button:
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chucks = get_text_chunks(raw_text)
                st.write(text_chucks)
            
            if not pdf_docs:
                st.error("Please upload at least one PDF file.")
        if pdf_docs:
            for pdf_file in pdf_docs:
                st.write(f"Uploaded: {pdf_file.name}")













if __name__ == "__main__":
    main()