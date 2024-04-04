#integrate our code with openAI api
import os 
from constants import key
from langchain.llms import OpenAI
import streamlit as st 
#from openai import GPT


os.environ["OPENAI_API_KEY"]=key

#streamlit fraamework 

st.title('langchain demo with openai api')
input_text = st.text_input("search the topic you want")

#openAi LLms
#llm = openai(temperature=0.8)
llm = OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))