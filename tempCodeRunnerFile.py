from PyPDF2 import PdfReader
from langchain_huggingface import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()
reader=PdfReader("my_writeup-2.pdf")
text=""
doc=[]
os.environ["HF_HOME"] = 'D:/HuggingFace_cache'
for pages in reader.pages:
    doc.append(pages.extract_text())


emb=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents=emb.embed_documents(doc)

print(documents)