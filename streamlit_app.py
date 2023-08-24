import streamlit as st
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain.document_loaders import *
from langchain.chains.summarize import load_summarize_chain
import tempfile
from langchain.docstore.document import Document

st.title("MapsGeneratorChat")

# Initialize state variables
chatbot_response = ""

# Generate a chatbot response for the given instruction
def chatbotResponse():
    chat = ChatOpenAI(
        model="gpt-3.5-turbo-16k",
        temperature=0.7
    )
    system_template = """You are a chatbot designed to generate responses based on given instructions."""
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_template = """Please generate a response for the given instruction."""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run({})
    return result # returns string   

# Display the generated chatbot response to the user
def display_response(chatbot_response):
    if chatbot_response != "":
        st.markdown(chatbot_response)

# Get input from the user
if st.button("Generate Chatbot Response"):
    chatbot_response = chatbotResponse()

# Call functions only if all user inputs are taken and the button is clicked.
display_response(chatbot_response)
