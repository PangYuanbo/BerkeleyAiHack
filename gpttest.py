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


breakfast = encode_image("image/banana.jpg")
print(breakfast)
lunch = encode_image("image/hamburger.jpg")
print(lunch)
dinner = encode_image("image/oreo.jpg")
print(dinner)

model = ChatOpenAI(model="gpt-4o").bind(response_format={"type": "json_object"})
response_format={ "type": "json_object" }
messages = [
    SystemMessage(
        content="Please analyze the calorie, water, protein, carbohydrates, cholesterol, fibroid, Sodium, Zinc, Copper, Manganese, Selenium, VitaminA, VitaminC, VitaminD, VitaminE, VitaminK, Thiamin, VitamnB12, which are produced by this three meals, according to the picture I gave you. VitaminD, VitaminE, VitaminK, Thiamin, VitamnB12. please send it to me using Json format.Just give the Json format of the following image."),
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
             "text": "dinner"},
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
