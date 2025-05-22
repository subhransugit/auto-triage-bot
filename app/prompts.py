# app/prompts.py

from langchain.prompts import PromptTemplate

support_prompt = PromptTemplate.from_template("""
You are a smart technical support assistant.
Answer questions using the provided context clearly and concisely.

Context:
{context}

Question:
{question}

Answer:
""")
