from fastapi import FastAPI
from Calculate_Todaymeal import food_pantry
from fastapi import FastAPI
from typing import Optional
from Calculate_Todaymeal import food_pantry
from Todaymeal_Evaluation import today_evaluation
from fastapi.middleware.cors import CORSMiddleware
from chat_youdotme import chat_bot
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from classes import Meal, Evaluation, Chat
@app.post("/todaymeal/")
def todaymeal(
        meal:Optional[ Meal]
):

    food = food_pantry(age=meal.age, height=meal.height, weight=meal.weight, others=meal.others, breakfast=meal.breakfast, lunch=meal.lunch,
                       dinner=meal.dinner)
    food.calculate_all()
    nutrition_needing = food.return_by_json()
    meal_nutrition = food.Ask_Gpt_food_nutrition(breakfast_annotations=meal.breakfast_annotations,lunch_annotations=meal.lunch_annotations,dinner_annotations=meal.dinner_annotations)
    return {
        "nutrition_needing": nutrition_needing,
        "meal_nutrition": meal_nutrition,
    }


@app.post("/Today_Evaluation/")
def Today_Evaluation(
        Evaluation: Optional[Evaluation]
):
    today= today_evaluation(nutrition_needing=Evaluation.nutrition_needing, meal_nutrition=Evaluation.meal_nutrition, others=Evaluation.others)
    evaluation=today.ask_for_evaluation()
    return {"Today_Evaluation": evaluation}

@app.post("/chat/")
def chat(
        chat: Optional[Chat]
):
    chatbot = chat_bot(information=chat.information, message=chat.message, img=chat.image, image_type=chat.image_type)
    if (chat.image=="0"):

        chat_response=chatbot.ask_for_chat()
        return {"chat_response": chat_response}
    else:
        chat_response=chatbot.aks_aws_claude()
        return {"chat_response": chat_response}



