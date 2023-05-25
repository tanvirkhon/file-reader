import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from pandasai.llm.openai import OpenAI
from pandasai import PandasAI

### OpenAI API Key
load_dotenv()

opeanai_api_key = os.getenv('OPENAI_API_KEY')

# Function for PandasAI to query a CSV file
def chat_with_csv(df, prompt):
    llm = OpenAI()
    pandas_ai = PandasAI(llm)
    result = pandas_ai.run(df, prompt=prompt)
    print(result)
    return result

st.set_page_config(page_title='Pricema AI', page_icon="🤖", layout="wide")

# Styling for the page
st.title('Chatbot CSV')
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

input_csv = st.file_uploader('Upload your CSV file', type=['csv'])

if input_csv is not None:

    col1, col2 = st.columns([1, 1])

    with col1:
        st.info("csv uploaded successfully")
        data = pd.read_csv(input_csv)
        st.dataframe(data)

    with col2:
        st.info("Chat with your CSV file")

        input_text = st.text_area("Enter your query")
        if input_text is not None:
            if st.button("Chat with CSV"):
                st.info("Your query: "+input_text)
                result = chat_with_csv(data, input_text)
                st.success(result)
