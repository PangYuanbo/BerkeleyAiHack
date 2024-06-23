import base64
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage

print(os.getcwd())
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_api_key
from langchain_openai import ChatOpenAI





# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


breakfast = encode_image("week/Day2/Breakfast/breakfast.webp")
print(breakfast)
lunch = encode_image("week/Day2/Lunch/lunch.webp")
print(lunch)
dinner = encode_image("week/Day2/Dinner/dinner.webp")
print(dinner)

model = ChatOpenAI(model="gpt-4o").bind(response_format={"type": "json_object"})
response_format={ "type": "json_object" }
messages = [
    SystemMessage(
        content="Please provide a detailed nutrition breakdown for three meals: breakfast, lunch, and dinner. Include the food name and values for calories, water, protein, carbohydrates, cholesterol, fibroid, sodium, zinc, copper, manganese, selenium, vitamin A, vitamin C, vitamin D, vitamin E, vitamin K, thiamin, and vitamin B12. The response should be in the following JSON format: {\"breakfast\": {\"food_name\": \"Oatmeal with bananas, walnuts, and honey\",\"calories\": 350,\"water\": 72,\"protein\": 7,\"carbohydrates\": 60,\"cholesterol\": 0,\"fibroid\": 6,\"sodium\": 10,\"zinc\": 1.1,\"copper\": 0.2,\"manganese\": 1.5,\"selenium\": 4.5,\"vitaminA\": 10,\"vitaminC\": 10,\"vitaminD\": 0,\"vitaminE\": 0.5,\"vitaminK\": 1.5,\"thiamin\": 0.15,\"vitaminB12\": 0},\"lunch\": {\"food_name\": \"Turkey wrap with avocado, tomato, lettuce, cucumber, and carrot sticks\",\"calories\": 400,\"water\": 85,\"protein\": 25,\"carbohydrates\": 45,\"cholesterol\": 35,\"fibroid\": 10,\"sodium\": 600,\"zinc\": 2.5,\"copper\": 0.1,\"manganese\": 0.3,\"selenium\": 18,\"vitaminA\": 100,\"vitaminC\": 30,\"vitaminD\": 0,\"vitaminE\": 2,\"vitaminK\": 20,\"thiamin\": 0.2,\"vitaminB12\": 1},\"dinner\": {\"food_name\": \"Grilled chicken with rice and mixed vegetables\",\"calories\": 500,\"water\": 80,\"protein\": 35,\"carbohydrates\": 60,\"cholesterol\": 85,\"fibroid\": 8,\"sodium\": 500,\"zinc\": 3,\"copper\": 0.2,\"manganese\": 0.5,\"selenium\": 25,\"vitaminA\": 150,\"vitaminC\": 40,\"vitaminD\": 0,\"vitaminE\": 1,\"vitaminK\": 30,\"thiamin\": 0.3,\"vitaminB12\": 1.5}}."),
    HumanMessage(
        content=[
            {"type": "text",
             "text": "breakfast"},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{breakfast}"},
            },
            {"type": "text",
             "text": "lunch"},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{lunch}"},
            },
            {"type": "text",
             "text": "Dinner"},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{dinner}"},
            },
        ]
    )
]
model.invoke(messages)
result = model.invoke(messages)
print(result.content)
