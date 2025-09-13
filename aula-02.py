from dotenv import load_dotenv
from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader

import os

load_dotenv()  # Carrega as variáveis do .env

# acessar as variáveis
# GOOGLE_API_KEY = userdata.get('GEMINI_API_KEY')

docs = []

for n in Path("./content/").glob("*.pdf"):
    try:
        loader = PyMuPDFLoader(str(n))
        docs.extend(loader.load())
        print(f"Carregado com sucesso arquivo {n.name}")
    except Exception as e:
        print(f"Erro ao carregar arquivo {n.name}: {e}")

print(f"Total de documentos carregados: {len(docs)}")

