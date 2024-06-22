from fastapi import HTTPException
from fastapi import Depends
from fastapi import FastAPI,File, UploadFile, Form
from Calculate_Todaymeal import food_pantry
app=FastAPI()
@app.post("/informain/")
def read_informain(
        name: str,
        age: int,
        height: float,
        weight: float,
        others: str,
        breakfast: str,
        lunch: str,
        dinner: str,

):
    food=food_pantry(age=age,height=height,weight=weight,others=others)
    food.calculate_all()
    return {
        "nutrition_needing": food.return_by_json(),
        "meal_nutrition": food.return_by_json(),
    }
