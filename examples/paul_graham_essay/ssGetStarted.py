import logging
import os
from typing import Callable, Dict, List, Optional

import openai
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

openai.api_key= os.getenv("OPENAI_API_KEY")

logging.basicConfig(level=logging.INFO)
os.chdir(os.path.dirname(__file__))
print(os.getcwd())

documents = SimpleDirectoryReader('data').load_data()
# index = GPTSimpleVectorIndex(documents)
# GPTSimpleVectorIndex.index.save_to_disk('ss_getStarted_index.json')
index = GPTSimpleVectorIndex.load_from_disk('ss_getStarted_index.json')
response = index.query("What did the author do growing up?")
print(response)

print(f"stop")