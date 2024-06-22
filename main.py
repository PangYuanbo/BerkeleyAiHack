from fastapi import FastAPI
from Calculate_Todaymeal import food_pantry
from fastapi import FastAPI

from Calculate_Todaymeal import food_pantry
from Todaymeal_Evaluation import today_evaluation
app = FastAPI()


@app.post("/todaymeal/")
def todaymeal(
        name: str,
        age: int,
        height: float,
        weight: float,
        others: str,
        breakfast: str,
        breakfast_annotations: str,
        lunch: str,
        lunch_annotations: str,
        dinner: str,
        dinner_annotations: str,

):

    food = food_pantry(age=age, height=height, weight=weight, others=others, breakfast=breakfast, lunch=lunch,
                       dinner=dinner)
    food.calculate_all()
    nutrition_needing = food.return_by_json()
    meal_nutrition = food.Ask_Gpt_food_nutrition(breakfast_annotations=breakfast_annotations,lunch_annotations=lunch_annotations,dinner_annotations=dinner_annotations)
    return {
        "nutrition_needing": nutrition_needing,
        "meal_nutrition": meal_nutrition,
    }


@app.get("/Today_Evaluation/")
def Today_Evaluation(
        nutrition_needing: str,
        meal_nutrition: str,
        others: str,
):
    today= today_evaluation(nutrition_needing=nutrition_needing, meal_nutrition=meal_nutrition, others=others)
    evaluation=today.ask_for_evaluation()
    return {"Today_Evaluation": evaluation}
