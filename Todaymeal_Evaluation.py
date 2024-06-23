import base64
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage

print(os.getcwd())
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_api_key
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o")


class today_evaluation:
    def __init__(self, nutrition_needing: str, meal_nutrition: str, others: str):
        self.nutrition_needing = nutrition_needing
        self.meal_nutrition = meal_nutrition
        self.other: str = others

    def ask_for_evaluation(self):
        messages = [
            SystemMessage(
                content="Please generate a Today's Diet report based on the user's particular situation, and total nutritional requirements, and total nutritional availability of the food."),
            HumanMessage(content="Special circumstances of the person: " + self.other),
            HumanMessage(content="The nutritional needs of the person: " + str(self.nutrition_needing)),
            HumanMessage(content="The nutritional content of the food: " + str(self.meal_nutrition))
        ]
        model.invoke(messages)
        result = model.invoke(messages)
        return result.content
