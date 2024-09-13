from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load the saved model
model = joblib.load('Part3_Model_IO/model.pkl')

# Define input data model
class PredictionInput(BaseModel):
    Pclass: int
    Sex: int
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked: int

@app.post("/predict")
def predict(input_data: PredictionInput):
    data = pd.DataFrame([input_data.dict()])
    try:
        prediction = model.predict(data)[0]
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# To run: uvicorn api:app --reload
