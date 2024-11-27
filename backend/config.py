import os
from dotenv import load_dotenv

load_dotenv()

name = os.getenv("NAME")
password = os.getenv("PASSWORD")