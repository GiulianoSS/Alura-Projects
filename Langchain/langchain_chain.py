from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableSequence
# from langchain.chains import LLMChain
# from langchain.chains import SimpleSequentialChain
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(
    model="mistral",
    temperature=0.5,
    api_key=os.getenv("OLLAMA_API_KEY"))

city_model = ChatPromptTemplate.from_template(
    "Sugira uma cidade dado meu interesse por {interesse}"
)

restaurants_model = ChatPromptTemplate.from_template(
    "Sugira restaurantes populates entre locais em {cidade}"
)

cultural_model = ChatPromptTemplate.from_template(
    "Sugira atividades e locais culturais em {cidade}"
)

city_chain = city_model | llm
restaurants_chain = restaurants_model | llm
cultural_chain = cultural_model | llm

chain = city_chain | restaurants_chain | cultural_chain

result = chain.invoke({"interesse": "praias"})
print(result.content)