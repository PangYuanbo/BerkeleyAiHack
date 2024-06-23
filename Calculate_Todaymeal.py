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
class food_pantry:
    def __init__(self, age, height, weight,others,breakfast,lunch,dinner):
        self.age = age
        self.height = height
        self.weight = weight
        self.other:str = others
        self.breakfast:str = breakfast
        self.lunch:str = lunch
        self.dinner:str = dinner
        self.calorie=0
        self.water=0
        self.protein=0
        self.BMI=0
        self.carbohydrates=0
        self.cholesterol=0
        self.fibroid=0
        self.Sodium=2300
        self.Zinc=11
        self.Copper=0.9
        self.Manganese=2.3
        self.Selenium=55
        self.VitaminA=900
        self.VitaminC=90
        self.VitaminD=15
        self.VitaminE=15
        self.VitaminK=120
        self.Thiamin=1.2
        self.VitamnB12=2.4
        self.Nutrition_needing = None
        self.meal_nutrition = None


    def calculate_calorie(self):
        self.calorie = 10*self.weight + 6.25*self.height - 5*self.age + 5
        return self.calorie

    def calculate_water(self):
        self.water = 30*self.weight
        return self.water

    def calculate_protein(self):
        self.protein = 0.8*self.weight
        return self.protein

    def calculate_BMI(self):
        self.BMI = self.weight/(self.height*self.height)
        return self.BMI

    def calculate_carbohydrates(self):
        self.carbohydrates = 0.5*self.weight
        return self.carbohydrates

    def calculate_cholesterol(self):
        self.cholesterol = 300
        return self.cholesterol

    def calculate_fibroid(self):
        self.fibroid = 25
        return self.fibroid

    def calculate_all(self):
        self.calculate_calorie()
        self.calculate_water()
        self.calculate_protein()
        self.calculate_BMI()
        self.calculate_carbohydrates()
        self.calculate_cholesterol()
        self.calculate_fibroid()
        return self.calorie, self.water, self.protein, self.BMI, self.carbohydrates, self.cholesterol, self.fibroid

    def return_by_json(self):
        self.Nutrition_needing =  {
            "BMI": self.BMI,
            "calorie": self.calorie,
            "water": self.water,
            "protein": self.protein,
            "carbohydrates": self.carbohydrates,
            "cholesterol": self.cholesterol,
            "fibroid": self.fibroid,
            "Sodium": self.Sodium,
            "Zinc": self.Zinc,
            "Copper": self.Copper,
            "Manganese": self.Manganese,
            "Selenium": self.Selenium,
            "VitaminA": self.VitaminA,
            "VitaminC": self.VitaminC,
            "VitaminD": self.VitaminD,
            "VitaminE": self.VitaminE,
            "VitaminK": self.VitaminK,
            "Thiamin": self.Thiamin,
            "VitamnB12": self.VitamnB12
        }
        return self.Nutrition_needing

    def Ask_Gpt_food_nutrition(self,breakfast_annotations,lunch_annotations,dinner_annotations):
        messages = [
            SystemMessage(
                content="Please analyze the calorie, water, protein, carbohydrates, cholesterol, fibroid, Sodium, Zinc, Copper, Manganese, Selenium, VitaminA, VitaminC, VitaminD, VitaminE, VitaminK, Thiamin, VitamnB12, which are produced by this three meals, according to the picture I gave you. VitaminD, VitaminE, VitaminK, Thiamin, VitamnB12. please send it to me using Json format.Just give the Json format of the following image."),
            HumanMessage(
                content=[
                    {"type": "text",
                     "text": "breakfast"+breakfast_annotations},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{self.breakfast}"},
                    },
                    {"type": "text",
                     "text": "lunch"+   lunch_annotations},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{self.lunch}"},
                    },
                    {"type": "text",
                     "text": "Dinner"+dinner_annotations},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{self.dinner}"},
                    },
                ]
            )
        ]
        model.invoke(messages)
        result = model.invoke(messages)
        self.meal_nutrition = result.content
        return self.meal_nutrition

