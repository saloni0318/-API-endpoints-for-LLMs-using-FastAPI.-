Multi-LLM LangChain Application

A simple AI application that integrates multiple Large Language Models (LLMs) using LangChain, FastAPI, LangServe, Ollama, and Streamlit to generate essays, poems, and explanations.



# Overview

This project demonstrates a Multi-LLM architecture using local models powered by Ollama.

The system supports:

- Multiple LLM integration
- FastAPI backend APIs
- LangServe model routing
- Streamlit frontend interface



#  Key Features

-  Multiple LLM support (Llama2, Mistral, Gemma)
-  FastAPI + LangServe backend
-  Streamlit interactive frontend
-  Essay generation
-  Poem generation
-  Simple explanation generator
-  Fully local execution using Ollama



# System Architecture

User Input
   ↓
Streamlit Frontend
   ↓
FastAPI + LangServe
   ↓
Prompt Templates
   ↓
Multiple LLMs (Ollama)
   ↓
Generated Response



