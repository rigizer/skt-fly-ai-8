# pip install openai
# pip install python-dotenv
import os
import openai
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

print('안녕하세요 AI 시인입니다. 당신이 원하는 주제로 아름다운 시를 지어드릴게요.')

subject = input('시의 주제를 입력해주세요: ')
content = input('시의 내용을 입력해주세요: ')

message = [
    {"role": "system", "content": "You are a AI Poet."},
    {"role": "user", "content": f'주제: {subject}\n내용: {content}\n이 주제와 내용으로 아름다운 시를 지어주세요.'}, 
]

response = openai.chat.completions.create(
    messages=message, 
    model=DEPLOYMENT_MODEL_NAME, 
    temperature=1, 
)

print(response.choices[0].message.content)