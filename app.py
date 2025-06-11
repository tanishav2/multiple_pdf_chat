import streamlit as st



def main():
    st.set_page_config(page_title="Chat with multple PDFs", page_icon=":books:")
    st.header("Chat with multiple PDFs :books:")
    st.text_input ("Ask a questions about your documents:")

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_files = st.file_uploader("Upload PDF files and click on Process", type=["pdf"], accept_multiple_files=True)
        process_button = st.button("Process")
        if process_button:
            if not pdf_files:
                st.error("Please upload at least one PDF file.")
            else:
                st.success(f"Processing {len(pdf_files)} PDF files...")
        if pdf_files:
            for pdf_file in pdf_files:
                st.write(f"Uploaded: {pdf_file.name}")













if __name__ == "__main__":
    main()