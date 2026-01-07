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

question = input('질문을 입력하세요: ')

message = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": question}
]

response = openai.chat.completions.create(
    messages=message, 
    model=DEPLOYMENT_MODEL_NAME, 
)

print(response.choices[0].message.content)