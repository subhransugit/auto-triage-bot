from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from retriever import get_retriever
from prompts import support_prompt

from dotenv import load_dotenv
load_dotenv()

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

def handle_query(query:str):
    retriever = get_retriever()
    chain = ConversationalRetrievalChain.from_llm(
        llm=OpenAI(temperature=0),
        retriever=retriever,
        combine_docs_chain_kwargs={"prompt": support_prompt},
        return_source_documents=True
        )
    # Inject memory manually
    result = chain.invoke({
        "question": query,
        "chat_history": memory.chat_memory.messages
    })

    # Save to memory explicitly
    memory.save_context({"question": query}, {"answer": result["answer"]})
    return result
