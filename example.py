from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do .env

# Agora você pode acessar as variáveis
secret_key = os.getenv("SECRET_KEY")