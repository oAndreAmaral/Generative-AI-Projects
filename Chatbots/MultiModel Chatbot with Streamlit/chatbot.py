from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from pyngrok import ngrok

# Get the variables that are in the .env file
load_dotenv() 

## ------------------------- Define the webpage -------------------------
# Define the initial page
st.set_page_config(
    page_title="IChatParrow",
    page_icon="🦜",
    layout="centered",
)

st.title("🦜IChatParrow")
user_prompt = st.chat_input("Ask IChatParrow a question...") # Create the input box in the webpage

# Select the model you want to use via dropdown box
model_options = {
    "Google": "gemini-2.5-flash",
    "Groq": "llama-3.3-70b-versatile"
}

# Initialize session state once
if "model_choice" not in st.session_state:
    st.session_state.model_choice = list(model_options.keys())[0] # store the model choice
    st.session_state.model_locked = False

choice = st.selectbox(
    "Choose the model:",
    list(model_options.keys()),
    key="model_choice",
    disabled=st.session_state.model_locked
)

# Lock the model after first interaction
if not st.session_state.model_locked:
    st.session_state.model_locked = True

model_name = model_options[choice]
st.write("Using model:", model_name)


## ----------------------------------------------------------------------

## ------------------------- Define the Chatbot -------------------------
# Initiate the chat history
if "chat_history" not in st.session_state: # If there is not chat history in the current section
    st.session_state.chat_history = [] # initiate the chat history

# Show data stream messages on the screen
for messages in st.session_state.chat_history:
    with st.chat_message(messages["role"]):
        st.markdown(messages["content"])

# initiate the LLM for that session according to the user choice
if model_name == "llama-3.3-70b-versatile":
    llm= ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.0
    )
elif model_name == "gemini-2.5-flash":
    llm= ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.0
    )

# If we have a user prompt
if user_prompt:
    st.chat_message("user").markdown(user_prompt) #give display of the message in the screen
    st.session_state.chat_history.append({"role":"user", "content": user_prompt}) # append the user message in the chat history

    # get the llm response given the chat history as input
    response = llm.invoke(
        input=[{"role":"system","content":"You are a helpfull assitant"}, *st.session_state.chat_history]
    )

    assistant_response = response.content # get the llm response
    st.session_state.chat_history.append({"role":"assistant","content":assistant_response}) # append the llm response to the chat history
    
    # display the llm response on the screen
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
## ----------------------------------------------------------------------