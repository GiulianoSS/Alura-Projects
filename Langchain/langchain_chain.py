from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

llm = ChatOllama(
    model="mistral",
    temperature=0.5,
    api_key=os.getenv("OLLAMA_API_KEY"))

city_model = ChatPromptTemplate.from_template(
    "Sugira uma cidade dado meu interesse por {interesse}"
)

restaurants_model = ChatPromptTemplate.from_template(
    Sugira restaurantes populates entre locais em {cidade}
)

cultural_model = ChatPromptTemplate.from_template(
    "Sugira atividades e locais culturais em {cidade}"
)

city_chain = LLMChain(prompt=city_model, llm=llm)
restaurants_chain = LLMChain(prompt=restaurants_model, llm=llm)
cultural_chain = LLMChain(prompt=cultural_model, llm=llm)
load_dotenv()