from fastapi import FastAPI
from Calculate_Todaymeal import food_pantry
from fastapi import FastAPI

from Calculate_Todaymeal import food_pantry
from Todaymeal_Evaluation import today_evaluation
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from classes import Meal, Evaluation
@app.post("/todaymeal/")
def todaymeal(
        meal: Meal
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


@app.get("/Today_Evaluation/")
def Today_Evaluation(
        Evaluation: Evaluation
):
    today= today_evaluation(nutrition_needing=Evaluation.nutrition_needing, meal_nutrition=Evaluation.meal_nutrition, others=Evaluation.others)
    evaluation=today.ask_for_evaluation()
    return {"Today_Evaluation": evaluation}

