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
        self.calorie = 10.0*self.weight + 6.25*self.height - 5.0*self.age + 5.0
        return self.calorie

    def calculate_water(self):
        self.water = 30.0*self.weight
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
                content="Please provide a detailed nutrition breakdown for three meals: breakfast, lunch, and dinner. Include the food name and values for calories, water, protein, carbohydrates, cholesterol, fibroid, sodium, zinc, copper, manganese, selenium, vitamin A, vitamin C, vitamin D, vitamin E, vitamin K, thiamin, and vitamin B12. The response should be in the following JSON format: {\"breakfast\": {\"food_name\": \"Oatmeal with bananas, walnuts, and honey\",\"calories\": 350,\"water\": 72,\"protein\": 7,\"carbohydrates\": 60,\"cholesterol\": 0,\"fibroid\": 6,\"sodium\": 10,\"zinc\": 1.1,\"copper\": 0.2,\"manganese\": 1.5,\"selenium\": 4.5,\"vitaminA\": 10,\"vitaminC\": 10,\"vitaminD\": 0,\"vitaminE\": 0.5,\"vitaminK\": 1.5,\"thiamin\": 0.15,\"vitaminB12\": 0},\"lunch\": {\"food_name\": \"Turkey wrap with avocado, tomato, lettuce, cucumber, and carrot sticks\",\"calories\": 400,\"water\": 85,\"protein\": 25,\"carbohydrates\": 45,\"cholesterol\": 35,\"fibroid\": 10,\"sodium\": 600,\"zinc\": 2.5,\"copper\": 0.1,\"manganese\": 0.3,\"selenium\": 18,\"vitaminA\": 100,\"vitaminC\": 30,\"vitaminD\": 0,\"vitaminE\": 2,\"vitaminK\": 20,\"thiamin\": 0.2,\"vitaminB12\": 1},\"dinner\": {\"food_name\": \"Grilled chicken with rice and mixed vegetables\",\"calories\": 500,\"water\": 80,\"protein\": 35,\"carbohydrates\": 60,\"cholesterol\": 85,\"fibroid\": 8,\"sodium\": 500,\"zinc\": 3,\"copper\": 0.2,\"manganese\": 0.5,\"selenium\": 25,\"vitaminA\": 150,\"vitaminC\": 40,\"vitaminD\": 0,\"vitaminE\": 1,\"vitaminK\": 30,\"thiamin\": 0.3,\"vitaminB12\": 1.5}}."),
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

