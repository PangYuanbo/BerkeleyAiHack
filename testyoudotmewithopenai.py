import os
import sys
from dotenv import load_dotenv
from langchain.retrievers.you import YouRetriever
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
ydc_api_key =os.getenv("YDC_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_api_key
os.environ["YDC_API_KEY"] = ydc_api_key
yr = YouRetriever()
model = "gpt-4o"
qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(model=model), chain_type="stuff", retriever=yr)
print(qa.run("What is the capital of France?and give me the weather in Paris with link."))