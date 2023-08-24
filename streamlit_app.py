import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from pydantic import ValidationError

st.title("MapsGeneratorChat")

# Initialize state variables
chatbot_response = ""
openai_api_key = ""

# Generate a chatbot response for the given instruction
def chatbotResponse(openai_api_key):
    chat = None
    try:
        chat = ChatOpenAI(
            model="gpt-3.5-turbo-16k",
            api_key=openai_api_key,
            temperature=0.7,
        )
    except ValidationError as e:
        st.error("Invalid API key. Please make sure you have entered a valid OpenAI API key.")
        return ""

    system_template = "You are a chatbot designed to generate responses based on given instructions."
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_template = "Please generate a response for the given instruction."
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    try:
        result = chat.generate_response(prompt=chat_prompt)
        return result  # returns string
    except Exception as e:
        st.error("An error occurred while generating chatbot response. Please try again.")
        return ""
    finally:
        if chat:
            chat.close()

# Display the generated chatbot response to the user
def display_response(chatbot_response):
    if chatbot_response:
        st.markdown(chatbot_response)

# Get input from the user
openai_api_key = st.text_input("Enter your OpenAI API key")

if st.button("Generate Chatbot Response"):
    chatbot_response = chatbotResponse(openai_api_key)

# Call functions only if all user inputs are taken and the button is clicked.
display_response(chatbot_response)
