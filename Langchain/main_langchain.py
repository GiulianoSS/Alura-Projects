from langchain_ollama import ChatOllama

# Variables
numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"

prompt = f"Crie um roteiro de viagem de {numero_de_dias} dias, para uma família com {numero_de_criancas} crianças, que gostam de {atividade}."
print(prompt)

llm = ChatOllama(
    model="mistral",
    temperature=0.5)

resposta = llm.invoke(prompt)
print(resposta.content)