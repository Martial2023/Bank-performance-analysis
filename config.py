from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

load_dotenv(dotenv_path)
DATABASE_URL = os.getenv('DATABASE_URL')
MONGO_URL = os.getenv('MONGO_URL')