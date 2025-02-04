from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("api_key")

model_name = os.getenv("MODEL_NAME")
mini_model_name = os.getenv("MINI_MODEL_NAME")
embedding_model = os.getenv("EMBEDDING_MODEL")

llm = ChatOpenAI(model=model_name)
llm2 = ChatOpenAI(model=mini_model_name)

embeddings = OpenAIEmbeddings(model=embedding_model)