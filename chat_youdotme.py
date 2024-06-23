import base64
import json
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
import requests
print(os.getcwd())
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
ydc_api_key =os.getenv("YDC_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_api_key
os.environ["YDC_API_KEY"] = ydc_api_key
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-4o").bind(response_format={"type": "json_object"})
class chat_bot:
    def __init__(self, information, message: str):
        self.information: str=information
        self.message: str=message

    def ask_for_chat(self):
        message = [SystemMessage(content="Please answer the user's questions based on weekly dietary intake, daily dietary health needs and nutrients already consumed that day. Use Json format to return the responses and output if an internet search is required and what the search is for.The response should be in the following JSON format: {\"response\": \"     \",\"using_search_engine\":\"True\",\"What to search\":\"Where is the sandwiches restaurant near UCB?\"}."   ),
                HumanMessage(content="all the information" + self.information),
                HumanMessage(content="message"+self.message)]
        model.invoke(message)
        result = model.invoke(message)
        data = json.loads(result.content)
        response = data.get('response', 'No response provided')
        using_search_engine = data.get('using_search_engine', 'No search engine information provided')
        what_to_search = data.get('What to search', 'No search query provided')
        if using_search_engine == 'True':
            search=self.ask_youdotcom(what_to_search)
            return search
        else:
            return response

    def ask_youdotcom(self, message: str) :
        url = "https://chat-api.you.com/research"

        payload = {
            "query": message,
            "chat_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
        }
        headers = {
            "X-API-Key": ydc_api_key,
            "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        return response.text


# a=chat(information="information",history="history",week_nutrition="week_nutrition", nutrition_needing_today="nutrition_needing_today", meal_nutrition_today="meal_nutrition_today", others="others", message="show me the restaurant near UCB?")
# print(a.ask_for_chat())