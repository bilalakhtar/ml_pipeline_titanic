import gradio as gr
import requests

def predict_with_model(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked):
    # Update this URL with your deployed FastAPI endpoint
    url = "http://127.0.0.1:8000/predict"  # Replace with deployed URL if needed
    data = {
        "Pclass": int(Pclass),
        "Sex": 1 if Sex == 'male' else 0,  # Assuming 'male' maps to 1, 'female' to 0
        "Age": float(Age),
        "SibSp": int(SibSp),
        "Parch": int(Parch),
        "Fare": float(Fare),
        "Embarked": {'S': 0, 'C': 1, 'Q': 2}[Embarked]  # Mapping Embarked to integers
    }
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

iface = gr.Interface(
    fn=predict_with_model,
    inputs=[
        gr.Number(label="Pclass"),
        gr.Number(label="Age"),
        gr.Number(label="SibSp"),
        gr.Number(label="Parch"),
        gr.Number(label="Fare"),
        gr.Dropdown(choices=['male', 'female'], label="Sex"),
        gr.Dropdown(choices=['S', 'C', 'Q'], label="Embarked")
    ],
    outputs="text",
    title="Titanic Survival Prediction",
    description="Enter the passenger details to predict survival on the Titanic."
)

iface.launch()
