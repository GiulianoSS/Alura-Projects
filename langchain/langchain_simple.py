from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

# Variables
numero_de_dias=7
numero_de_criancas=2
atividade="praia"

template = PromptTemplate.from_template(
    f"Crie um roteiro de viagem de {numero_de_dias} dias, para uma família com {numero_de_criancas} crianças, que gostam de {atividade}."
)

prompt = template.format(dias=numero_de_dias,
                        criancas=numero_de_criancas,
                        atividade=atividade)

print(prompt)

llm = ChatOllama(
    model="mistral",
    temperature=0.5,
    api_key=os.getenv("OLLAMA_API_KEY"))

resposta = llm.invoke(prompt)
print(resposta.content)