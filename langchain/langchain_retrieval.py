from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableSequence, RunnableLambda
from langchain.globals import set_debug
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationSummaryMemory
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_ollama import OllamaEmbeddings
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
import os
from dotenv import load_dotenv

load_dotenv()
set_debug(True)

llm = ChatOllama(
    model="mistral",
    temperature=0.5,
    api_key=os.getenv("OLLAMA_API_KEY"))

loader = TextLoader("data/GTB_gold_Nov23.txt", encoding="utf-8")
document = loader.load()
chunker = CharacterTextSplitter(chunk_size=1000)
texts = chunker.split_documents(document)
print(texts)

embeddings = OllamaEmbeddings()
db = FAISS.from_documents(texts, embeddings)

qa_chain = RetrievalQA.from_chain_type(llm, retriever=db.as_retriever())

question = "Como devo proceder caso tenha um item comprado roubado"
result = qa_chain.invoke({"query": question})
# print(result)