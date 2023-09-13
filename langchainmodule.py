from langchain import FAISS
from langchain.document_loaders import UnstructuredFileLoader
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
import sentence_transformers
import torch
device = torch.device('cuda')
#ckpt="m3e-large"
ckpt="m3e-base"
embeddings = HuggingFaceEmbeddings(model_name=ckpt)
embeddings.client = sentence_transformers.SentenceTransformer(ckpt,device=device)

def similar_context(question,context):
    with open("tempor_context.txt","w",encoding="utf-8")as f:
        f.write(context)
    filepath2 = "tempor_context.txt"
    vs_path2 = f"""./vector_store/tempor_context_FAISS"""
    docs2 = []
    loader2 = UnstructuredFileLoader(filepath2, mode="elements")
    docs2 += loader2.load()
    vector_store2 = FAISS.from_documents(docs2, embeddings)
    vector_store2.save_local(vs_path2)
    mem=""
    search_type = "similarity"  # Specify the search type, e.g., "nearest_neighbors" or "semantic_search"
    results = vector_store2.search(question, search_type, k=3)  # Replace 10 with the desired number of results
    for result in results:
        mem += result.page_content + "\n"
    #mem = mem.replace("<6>", "\n")
    mem=mem.strip()
    return mem