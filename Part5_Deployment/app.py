import gradio as gr
import requests

def predict_with_model(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked):
    # Replace with your FastAPI endpoint
    url = "http://127.0.0.1:8000/predict"
    data = {
        "Pclass": int(Pclass),
        "Sex": int(Sex),
        "Age": float(Age),
        "SibSp": int(SibSp),
        "Parch": int(Parch),
        "Fare": float(Fare),
        "Embarked": int(Embarked)
    }
    response = requests.post(url, json=data)
    return response.json()

iface = gr.Interface(
    fn=predict_with_model,
    inputs=[
        gr.inputs.Number(label="Pclass"),
        gr.inputs.Number(label="Sex (0 for male, 1 for female)"),
        gr.inputs.Number(label="Age"),
        gr.inputs.Number(label="SibSp"),
        gr.inputs.Number(label="Parch"),
        gr.inputs.Number(label="Fare"),
        gr.inputs.Number(label="Embarked (0, 1, 2 for ports)")
    ],
    outputs="text",
    title="Titanic Survival Prediction",
    description="Enter the passenger details to predict survival on the Titanic."
)

iface.launch()
