import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')

#prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","Your are a helpful assistant that helps people find information."),
        ("user","Question:{question}")
    ]
)

##streamlit framework
st.title("💬 Ollama(Gemma Model) + LangChain Chatbot")
input_text=st.text_input("What Question do you have?")

llm=Ollama(model="gemma:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))