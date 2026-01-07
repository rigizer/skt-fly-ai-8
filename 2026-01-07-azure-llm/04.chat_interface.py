import os
import openai
import streamlit as st
from dotenv import load_dotenv

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

# OpenAI API 호출
def get_response(messages):
    try:
        response = openai.chat.completions.create(
            messages=messages,
            model=DEPLOYMENT_MODEL_NAME,
            temperature=1,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI 설정
st.title('Chat with Azure OpenAI LLM')
st.write('Type your messages below and get responses from the OpenAI model.')

# 채팅 기록 초기화
if 'messages' not in st.session_state:
    st.session_state.messages = []

    # st.chat_message("Hello! How can I assist you today?")

# 채팅 메시지 표시
for message in st.session_state.messages:
    st.chat_message(message['role']).write(message['content'])

# 사용자 입력 처리
if prompt := st.chat_input("Type your message here..."):
    # 사용자 메시지 추가
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("AI가 생각하는 중...", show_time=True):
        # 모델 응답 받기
        response = get_response(st.session_state.messages)

        # 모델 메시지 추가
        st.chat_message("assistant").write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})