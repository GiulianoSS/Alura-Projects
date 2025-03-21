from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableSequence
from langchain.globals import set_debug
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()
set_debug(True)

llm = ChatOllama(
    model="mistral",
    temperature=0.5,
    api_key=os.getenv("OLLAMA_API_KEY"))

messages = [
        "Quero visitar um lugar no Brasil famoso por suas praias e cultura. Pode me recomendar?",
        "Qual é o melhor período do ano para visitar em termos de clima?",
        "Quais tipos de atividades ao ar livre estão disponíveis?",
        "Alguma sugestão de acomodação eco-friendly por lá?",
        "Cite outras 20 cidades com características semelhantes às que descrevemos até agora. Rankeie por mais interessante, incluindo no meio ai a que você já sugeriu.",
        "Na primeira cidade que você sugeriu lá atrás, quero saber 5 restaurantes para visitar. Responda somente o nome da cidade e o nome dos restaurantes.",
]

long_chat = ""
for message in messages:
    long_chat += f"Usuário: {message}\n"
    long_chat += f"AI: "

    model = PromptTemplate(template=long_chat,
                           input_variables=[""])
    chain = model | llm | StrOutputParser()
    result = chain.invoke(input={})
    #print(result)

    long_chat += result + "\n"
    print(long_chat)