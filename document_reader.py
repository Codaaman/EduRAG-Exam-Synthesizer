from sklearn.metrics.pairwise import cosine_similarity
from documents_uploader import document_ritrival,embeddings_ritrival
from langchain_huggingface import HuggingFaceEmbeddings



def query(q:str)->str:
    emb=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    user_emb=emb.embed_query(q)

    score=cosine_similarity([user_emb],embeddings_ritrival())[0]

    index,score=sorted(list(enumerate(score)),key=lambda x:x[1])[-1]

    return document_ritrival()[index]

