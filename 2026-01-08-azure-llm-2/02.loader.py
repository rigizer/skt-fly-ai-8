# pdf loader

## pip install pypdf
## pip install cryptography

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('C:\\Users\\SKT019\\Documents\\skt-fly-ai-8\\2026-01-08-azure-llm-2\\Owners_Manual.pdf')
pages = loader.load_and_split()

# print(f'Number of pages: {len(pages)}')
# print(pages[9].page_content)

# word loader

## pip install docx2txt
# from langchain_community.document_loaders import Docx2txtLoader

# =================================

# pip install tiktoken

import tiktoken

tokenizer = tiktoken.get_encoding('cl100k_base')

def tiktoken_len(text: str) -> int:
    tokens = tokenizer.encode(text)
    return len(tokens)


# print(tiktoken_len('I Love You'))
# print(tiktoken_len(pages[9].page_content))

# Text를 자르는 Splitter

# pip install langchain-text-splitters

from langchain_text_splitters import RecursiveCharacterTextSplitter
# 자르기 위한 칼을 준비
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,  # 겹치는 부분, 연속적 (10%정도)
    length_function=tiktoken_len,
)

texts = text_splitter.split_text(pages[9].page_content)
print(texts[0])
print('-' * 100)
print(texts[1])
print('-' * 100)
print(texts[2])
print('-' * 100)



