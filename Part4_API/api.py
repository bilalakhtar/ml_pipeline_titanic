!ngrok config add-authtoken 2l1Ouypfij2gu4P49kAE42Xoctz_7bwkBVzykP37A9R32foUy

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import uvicorn
import nest_asyncio
from pyngrok import ngrok

# Initialize the FastAPI app
app = FastAPI()

# Load the saved model
try:
    model = joblib.load('/content/drive/MyDrive/Colab Notebooks/model.pkl')
except FileNotFoundError:
    raise RuntimeError("Model file not found. Ensure 'model.pkl' is in the correct path.")

# Define input data model using Pydantic
class PredictionInput(BaseModel):
    Pclass: int
    Sex: int
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked: int

# Define the prediction endpoint
@app.post("/predict")
def predict(input_data: PredictionInput):
    # Convert input data to DataFrame
    data = pd.DataFrame([input_data.dict()])
    try:
        # Make prediction
        prediction = model.predict(data)[0]
        return {"prediction": prediction}
    except Exception as e:
        # Handle prediction errors
        raise HTTPException(status_code=400, detail=f"Prediction failed: {str(e)}")

# Set up Ngrok for tunneling and run the server
if __name__ == "__main__":
    # Set up Ngrok tunnel to expose the server
    ngrok_tunnel = ngrok.connect(8000)
    print('Public URL:', ngrok_tunnel.public_url)
    
    # Apply asyncio fix for running inside Jupyter or similar environments
    nest_asyncio.apply()
    
    # Run the Uvicorn server
    uvicorn.run(app, port=8000)
