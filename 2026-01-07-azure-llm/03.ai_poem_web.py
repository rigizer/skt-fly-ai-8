# pip install openai
# pip install python-dotenv
# pip install streamlit
import os
import time
import openai
import streamlit as st
from dotenv import load_dotenv

# streamlit run 03.ai_poem_web.py

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
AZURE_OPENAI_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT')
OPENAI_API_TYPE = os.getenv('OPENAI_API_TYPE')
AZURE_OPENAI_API_VERSION = os.getenv('AZURE_OPENAI_API_VERSION')
DEPLOYMENT_MODEL_NAME = os.getenv('DEPLOYMENT_MODEL_NAME')

openai.api_key = OPENAI_API_KEY
openai.azure_endpoint = AZURE_OPENAI_ENDPOINT
openai.api_type = OPENAI_API_TYPE
openai.api_version = AZURE_OPENAI_API_VERSION

st.title('안녕하세요 AI 시인입니다.')
st.write('당신이 원하는 주제로 아름다운 시를 지어드릴게요.')

print('안녕하세요 AI 시인입니다. 당신이 원하는 주제로 아름다운 시를 지어드릴게요.')

subject = st.text_input('시의 주제를 입력해주세요', key='subject')
content = st.text_area('시의 내용을 입력해주세요', key='content')

message = [
    {"role": "system", "content": "You are a AI Poet."},
    {"role": "user", "content": f'주제: {subject}\n내용: {content}\n이 주제와 내용으로 아름다운 시를 지어주세요.'}, 
]

button_clicked = st.button('시 만들기')

if button_clicked:
    with st.spinner("열심히 시를 짓는 중...", show_time=True):
        response = openai.chat.completions.create(
            messages=message, 
            model=DEPLOYMENT_MODEL_NAME, 
            temperature=1, 
        )

        st.write(response.choices[0].message.content)
        # st.text_area('', value=response.choices[0].message.content, height=300)
