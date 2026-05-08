from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
from langchain_community.llms import Ollama
import uvicorn

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API Server"
)

# Multiple LLMs
llama_llm = Ollama(model="llama2")
mistral_llm = Ollama(model="mistral")
gemma_llm = Ollama(model="gemma")

# Prompts
prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words"
)

prompt2 = ChatPromptTemplate.from_template(
    "Write me a poem about {topic} for a 5 years child with 100 words"
)

prompt3 = ChatPromptTemplate.from_template(
    "Explain {topic} in simple terms"
)


add_routes(
    app,
    llama_llm,
    path="/llama"
)

add_routes(
    app,
    mistral_llm,
    path="/mistral"
)

add_routes(
    app,
    gemma_llm,
    path="/gemma"
)


add_routes(
    app,
    prompt1 | llama_llm,
    path="/essay"
)

add_routes(
    app,
    prompt2 | mistral_llm,
    path="/poem"
)

add_routes(
    app,
    prompt3 | gemma_llm,
    path="/explain"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)