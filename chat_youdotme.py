import base64
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage

print(os.getcwd())
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_api_key
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-4o").bind(response_format={"type": "json_object"})
class chat:
    def __init__(self, information,history,week_nutrition: str, nutrition_needing_today: str, meal_nutrition_today: str, others: str, message: str):
        self.information: str=information
        self.history: str=history
        self.week_nutrition: str=week_nutrition
        self.nutrition_needing_today: str=nutrition_needing_today
        self.meal_nutrition_today: str=meal_nutrition_today
        self.others: str=others
        self.message: str=message

    def ask_for_chat(self):
        message = [SystemMessage(content="Please answer the user's questions based on weekly dietary intake, daily dietary health needs and nutrients already consumed that day. Use Json format to return the responses and output if an internet search is required and what the search is for.The response should be in the following JSON format: {\"response\": \"     \",\"using_search_engine\":\"True\",\"What to search\":\"Where is the sandwiches restaurant near UCB?\"}."   ),
                    HumanMessage(content="week_nutrition"+self.week_nutrition),
                    HumanMessage(content="nutrition_needing_today"+self.nutrition_needing_today),
                    HumanMessage(content="meal_nutrition_today"+self.meal_nutrition_today),
                    HumanMessage(content="others"+self.others),
                   HumanMessage(content="message_history"+self.history),
                   HumanMessage(content="message"+self.message)]
        response = model.ask(message)

        return response

a=chat(information="information",history="history",week_nutrition="week_nutrition", nutrition_needing_today="nutrition_needing_today", meal_nutrition_today="meal_nutrition_today", others="others", message="message")
