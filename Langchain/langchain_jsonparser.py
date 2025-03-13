from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableSequence
from langchain.globals import set_debug
# from langchain_core.pydantic_v1 import Field, BaseModel
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
# from langchain.chains import LLMChain
# from langchain.chains import SimpleSequentialChain
import os
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

city_chain = city_model | llm
restaurants_chain = restaurants_model | llm
cultural_chain = cultural_model | llm

# chain = (city_chain | restaurants_chain | cultural_chain).with_config(verbose=True)
chain = (city_chain).with_config(verbose=True)

result = chain.invoke({"interesse": "praias"})
print(result)