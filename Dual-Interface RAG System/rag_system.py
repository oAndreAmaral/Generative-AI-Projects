import os
from dotenv import load_dotenv

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA

from llms_access.EndpointLLM import EndpointLLM

load_dotenv() # read the environmental variables

working_directory = os.path.dirname(os.path.abspath((__file__))) # Get the working directory where is this python script

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

# Models instanciation
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.0
)

def ingestion_pdf_to_vectordatabase(file_name):

    # Loading the directory in the loader with the specific folders and load the documents
    loader = PyPDFLoader(f"{working_directory}/{file_name}")

    documents = loader.load() # store the files in the variable list documents (length = number of documents ||  documents[x] - gives the document x content)

    # Split the documents into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 2000,
        chunk_overlap = 200
    )

    text_chunks = text_splitter.split_documents(documents)

    # Store the text chunks in the database
    vector_store = Chroma(
        persist_directory = f"{working_directory}/doc_vector_db",
        embedding_function=embedding
    )

    vector_store.add_documents(text_chunks) # with add_documents we can append the embeddings from new documents instead of replace the old one.

    return 0

def retrieval_vectordatabase_to_response(user_question):

    # Load the vector data from the database
    vector_store = Chroma(
        embedding_function=embedding,
        persist_directory=f"{working_directory}/doc_vector_db"
    )

    # Create a retriever
    retriever = vector_store.as_retriever(search_kwargs={"k": 2})

    # Prepare the Question and Awnser chain
    qa_chain = RetrievalQA.from_chain_type(
        llm = llm,
        chain_type = "stuff",
        retriever = retriever,
        return_source_documents = True
    )

    # get the response from the llm
    response = qa_chain.invoke({"query":user_question})
    answer = response['result']

    source_names = []

    for source in response["source_documents"]:
        file_path = source.metadata["source"]
        source_name = os.path.basename(file_path)
        source_names.append(source_name)

    unique_source_names = list(set(source_names))

    return answer, unique_source_names