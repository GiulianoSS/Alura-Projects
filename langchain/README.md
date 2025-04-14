# LangChain Project
This repository contains code and resources developed during a course on [LangChain at Alura](https://cursos.alura.com.br/course/langchain-python-ferramentas-llm-openai). [LangChain](https://python.langchain.com/docs/introduction/) is a framework for building applications with LLMs (Large Language Models) that use chains and agents to interact with data and APIs.

## Setup and Installation
Before running the code, you must set up the environment and install the required dependencies.

⚙️ **Note**: The original course was designed to work with OpenAI's API, which was free at the time.
💡 This version has been fully adapted to work with Ollama, enabling you to run LLMs locally without needing a paid API key.

## Environment Setup
Install [Miniconda](https://www.anaconda.com/download/) to manage your environment.

- Create a virtual environment:
```bash
conda create --name langchain-env python=3.x
```

Install the necessary packages using requirements.txt:

```bash
pip install -r requirements.txt
```
Download and install Ollama to run the model locally ([Download Ollama for macOS/Linux/Windows](https://ollama.com/download/windows)).

Set your API key manually inside your virtual environment for local API access (**optional**).

## Files in the Project
**langchain_buffer_memory.py**
This script implements buffer memory management using LangChain. It allows for storing and retrieving information within the same session to enhance context in conversations or workflows.

**langchain_buffer_window.py**
This script utilizes a windowed memory approach, which can store a fixed number of prior interactions or states within the session. It helps to manage the context effectively.

**langchain_chain.py**
Defines a chain that executes a sequence of operations or queries. Each operation can interact with external data or APIs, and the output of one step is used as the input for the next.

**langchain_jsonparser.py**
This script parses JSON data to be used within LangChain applications. It can extract, filter, or transform data stored in JSON format, making it easy to integrate into LangChain chains.

**langchain_lcel_join.py**
This script is likely responsible for joining multiple data sources or chains in LangChain using the LCEL (LangChain Execution Language) feature. It could be about integrating different data sources or chaining different processing steps together.

**langchain_lcel.py**
Handles operations related to LCEL, which is a specific feature in LangChain used to define workflows and logic in the execution of tasks. This script might be setting up specific logic or operations.

**langchain_memory.py**
Defines memory handling for LangChain models, enabling the model to remember certain facts or data across different interactions or states in the application.

**langchain_retrieval.py**
Focuses on implementing a retrieval-based approach for LangChain, possibly interacting with external databases or APIs to fetch relevant information based on user input.

**langchain_retrieval.pdf**
A PDF document that likely explains or provides details on implementing retrieval within LangChain, possibly a reference to how to integrate LangChain with search engines or document databases.

**langchain_simple.py**
A simplified version of LangChain that demonstrates basic functionality, potentially showcasing how to use LangChain with minimal setup or dependencies.

**langchain_summary.py**
This script likely generates summaries from documents or large data sets, utilizing LangChain's ability to interact with language models and process large chunks of text for summarization.

**ollama_simple.py**
A simple script that uses Ollama (the local LLM API) to interact with LangChain. This script likely demonstrates basic interaction with a language model via Ollama, enabling local processing of natural language tasks.

# Folder Structure
data/: Contains datasets or files used in LangChain retrieval and other scripts.

requirements.txt: Lists the necessary dependencies to run the project.

README.md: This file, explaining the project and setup instructions.