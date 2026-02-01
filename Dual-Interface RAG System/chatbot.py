import os
import streamlit as st

# get the LLM RAG functions
from rag_system import ingestion_pdf_to_vectordatabase, retrieval_vectordatabase_to_response

# set the directory
working_directory = os.path.dirname(os.path.abspath((__file__)))

# STREAMLIT: set the title for the streamlit app
st.title("My Chatbot")

# STREAMLIT: upload multiple pdf files
uploaded_files = st.file_uploader("Upload a PDF file", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        if uploaded_file is not None:

            save_path = os.path.join(working_directory, uploaded_file.name) # generate the path where to save the file
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer()) # save the file in the right directory

            # LLM RAG: ingestion process
            process_document = ingestion_pdf_to_vectordatabase(uploaded_file.name)

    st.info("Document Processed Successefully") # inform the user about the upload in the chatbot

# STREAMLIT: get the user input

user_question = st.text_area("What is your question about the document?")

if st.button("Answer"):

    # LLM RAG: retrieval process
    answer, source_name = retrieval_vectordatabase_to_response(user_question)

    # STREAMLIT: print the response and source
    st.markdown("Agent Response:")
    st.markdown(answer)
    st.markdown(source_name)