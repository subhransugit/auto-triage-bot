from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from retriever import get_retriever

from dotenv import load_dotenv
load_dotenv()

def handle_query(query:str):
    retriever = get_retriever()
    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=0),
        retriever=retriever,
        return_source_documents=True
    )
    result = qa_chain.invoke({"query": query})
    return result  # a dict with keys: 'result', 'source_documents'
