from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, AIMessagePromptTemplate
from langchain.schema.runnable import RunnableSequence
from langchain.globals import set_debug
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from pydantic import BaseModel, Field
import os
from operator import itemgetter
from dotenv import load_dotenv

load_dotenv()
set_debug(True)

class Destiny(BaseModel):
    cidade: str = Field(..., description="cidade a visitar")
    motivo: str = Field(..., description="motivo pelo qual é interessante visitá-la")

llm = ChatOllama(
    model="mistral",
    temperature=0.5,
    api_key=os.getenv("OLLAMA_API_KEY"))

parser = JsonOutputParser(pydantic_object=Destiny)

city_model = PromptTemplate(
    template = """Sugira uma cidade dado meu interesse por {interesse}.
    {output_format}""",
    input_variables = ["interesse"],
    partial_variables = {"output_format": parser.get_format_instructions()}

)

restaurants_model = ChatPromptTemplate.from_template(
    "Sugira restaurantes populares entre locais em {cidade}"
)

cultural_model = ChatPromptTemplate.from_template(
    "Sugira atividades e locais culturais em {cidade}"
)

final_model = ChatPromptTemplate.from_messages(
    [
    AIMessagePromptTemplate.from_template("Sugestão de viagem para a cidade: {cidade}"),
    AIMessagePromptTemplate.from_template("Restaurantes que você não pode perder: {restaurants}"),
    AIMessagePromptTemplate.from_template("Atividades e locais culturais recomendados: {cultural_locations}"),
    SystemMessagePromptTemplate.from_template("Combine as informações das cadeias anteriores em 2 parágrafos coerentes")
    ]
)

part1 = city_model | llm | parser
part2 = restaurants_model | llm | StrOutputParser()
part3 = cultural_model | llm | StrOutputParser()
part4 = final_model | llm | StrOutputParser()

chain = (part1 | 
         {"restaurants": part2, 
          "cultural_locations": part3,
          "cidade" : itemgetter("cidade")}
          | part4)

# print(city_model.invoke({"interesse": "praias"}))

result = chain.invoke({"interesse": "praias"})
print(result)