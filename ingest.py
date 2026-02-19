from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

loader = TextLoader("data/sample_docs.txt")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

db = Chroma.from_documents(chunks, OpenAIEmbeddings(), persist_directory="db")
db.persist()

print("Documents ingested successfully")

