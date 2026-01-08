# pip install openai
# pip install langchain langchain-core langchain-community
# pip install langchain-openai
# pip install 

import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.callbacks import StreamingStdOutCallbackHandler
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

# chat_llm = AzureChatOpenAI(
#     deployment_name='dev-gpt-4.1-mini', 
#     temperature=1, 
# )

chat_llm = AzureChatOpenAI(
    deployment_name='dev-gpt-4.1-mini', 
    temperature=1, 
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
)

# response = chat_llm.invoke('What python is most popular language? answer in Korean')

# messages = [
#     SystemMessage(content="You are a helpful assistant that translates English to Korean."),
#     HumanMessage(content="I love programming."),
# ]'

messages = [
    SystemMessage(content="너는 공부 계획을 세우는 스터디 플래너야. 주제를 입력 받으면 이를 학습할 수 있는 계획을 세워줘"),
    HumanMessage(content="Large Language Model"),
]

response = chat_llm.invoke(messages)

print(response.content)