from dotenv import load_dotenv # pip install python-dotenv
import os

load_dotenv()

print(os.getenv('nome'))

