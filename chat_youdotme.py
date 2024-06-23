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

    def ask