from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes
from dotenv import load_dotenv
load_dotenv()

model=ChatGroq(model="llama-3.1-8b-instant", groq_api_key=groq_api_key)

#1. Create Prompt Template
generic_template="Translate the following into {language}:"

prompt=ChatPromptTemplate.from_messages(
    [
        ("system",generic_template),
        ("user","{text}")
    ]
)

parser=StrOutputParser()

chain=prompt|model|parser

groq_api_key=os.getenv("GROQ_API_KEY")


#App Defination

app=FastAPI(title="LangChain Server",
            version="1.0")

add_routes(app, chain, path="/chain")


if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1",port=8000)
