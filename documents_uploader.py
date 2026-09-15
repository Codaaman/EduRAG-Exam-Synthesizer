from PyPDF2 import PdfReader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores.pgvector import PGVector
from langchain_core.documents import Document
import os
from dotenv import load_dotenv
import ast
import psycopg2 as db
from sklearn.metrics.pairwise import cosine_similarity


load_dotenv()
os.environ["HF_HOME"] = 'D:/HuggingFace_cache'
print(os.getenv("HF_HOME"))


conection="postgresql+psycopg2://postgres:aman9935@localhost:5432/question_paper_vactor"
collection_name="q-pdf"

reader=PdfReader("my_writeup-2.pdf")
text=""
doc=[]
for pages in reader.pages:
    doc.append(pages.extract_text())


#emb=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
#documents=emb.embed_documents(doc)
#documents=[Document(page_content=k)for k in doc]
#db=PGVector.from_documents(embedding=emb,documents=documents,connection_string=conection,collection_name=collection_name)
#print(emb)



def conection_estabils():
    conn = db.connect(
        dbname="question_paper_vactor",
        user="postgres",
        password="aman9935",
        host="localhost",
        port="5432" 
    )

    return conn



def document_ritrival():

    cur=conection_estabils().cursor()

    '''cur.execute("SELECT document FROM langchain_pg_embedding")
    rows = cur.fetchall()  # sabhi rows fetch karega
    for row in rows:
        documents.append(row[0])'''

    #cur.execute("SELECT document FROM langchain_pg_embedding WHERE collection = %s", ('Pdfs_collection',))
    cur.execute("SELECT document FROM langchain_pg_embedding")
    documents = [row[0] for row in cur.fetchall()]

    return documents

def embeddings_ritrival():
    embed=[]

    cur=conection_estabils().cursor()

    '''cur.execute("SELECT document FROM langchain_pg_embedding")
    rows = cur.fetchall()  # sabhi rows fetch karega
    for row in rows:
        documents.append(row[0])'''

    cur.execute("SELECT embedding FROM langchain_pg_embedding")
    rows = cur.fetchall()  # sabhi rows fetch karega

    for row in rows:
        value=ast.literal_eval(row[0])
        embed.append(value)
        print(embed)

    return embed


