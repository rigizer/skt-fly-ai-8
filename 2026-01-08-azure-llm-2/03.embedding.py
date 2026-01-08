from dotenv import load_dotenv
from langchain_openai import AzureOpenAIEmbeddings

load_dotenv()

embeddings = AzureOpenAIEmbeddings(
    azure_deployment='dev-text-embedding-3-small', 
    chunk_size=500, 
)

examples = [
    '안녕하세요', 
    '제 이름은 홍길동 입니다.', 
    '이름이 무엇인가요?', 
    '랭체인은 유용합니다', 
    'Hello, World!', 
]

# vectorizing embedding
# results = embeddings.embed_documents(examples)

# print(len(results))
# print(results[0])

## numpy를 통한 연산 수행
from numpy import dot
from numpy.linalg import norm
import numpy as np

## 코사인 유사도 함수
def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return dot(a, b) / (norm(a) * norm(b))


def calc_similarity(a, b):
    x = embeddings.embed_query(a)
    y = embeddings.embed_query(b)

    return str(cosine_similarity(x, y) * 100) + '%'

print(calc_similarity(
    '이 대회에서 언급된 이름은 무엇입니까?', 
    '제 이름은 홍길동 입니다.')
)

print(calc_similarity(
    '안녕 세상아!', 
    'Hello, World!'
))

print(calc_similarity(
    '헬로 월드', 
    'Hello, World!'
))




