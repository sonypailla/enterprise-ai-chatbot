from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def get_chatbot():
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    db = Chroma(persist_directory="db", embedding_function=OpenAIEmbeddings())
    retriever = db.as_retriever(search_kwargs={"k": 3})

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever
    )
    return qa

