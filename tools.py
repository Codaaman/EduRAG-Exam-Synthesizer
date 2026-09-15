from exa_py import Exa
from dotenv import load_dotenv
import os

load_dotenv()
key=os.getenv("EXA_API")

narad=Exa(key)


def searcha(query:str)->str:
    """Search the web"""
    result=narad.search(query)
    return result