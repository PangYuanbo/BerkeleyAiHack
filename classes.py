from pydantic import BaseModel


class Meal(BaseModel):
    name: str
    age: int
    height: float
    weight: float
    others: str
    breakfast: str
    breakfast_annotations: str
    lunch: str
    lunch_annotations: str
    dinner: str
    dinner_annotations: str


class Evaluation(BaseModel):
    nutrition_needing: str
    meal_nutrition: str
    others: str

class Chat(BaseModel):
    information: str
    history: str
    week_nutrition: str
    nutrition_needing_today: str
    meal_nutrition_today: str
    others: str
    message: str
