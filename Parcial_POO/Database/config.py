from dotenv import load_dotenv
import os

# Carga automáticamente el archivo .env más cercano en la jerarquía
load_dotenv()

SDK = os.getenv('SDK')
URL_DB = os.getenv('URL_DB')
