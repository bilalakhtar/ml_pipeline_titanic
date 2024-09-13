# ml_pipeline_titanic
# Project: Titanic Survival Prediction Pipeline

This project demonstrates a complete machine learning pipeline to predict the survival of Titanic passengers, from data cleaning to model deployment.

## Prerequisites
- Python 3.7+
- Required Libraries: pandas, scikit-learn, joblib, fastapi, uvicorn, gradio, nest_asyncio, pyngrok

Install the required libraries using the following command:
  '''
  pip install pandas scikit-learn joblib fastapi uvicorn gradio nest_asyncio pyngrok
  '''
Steps to Run
Part 1: Data Cleaning
Navigate to the Part1_Data_Cleaning folder.

Run the script:

bash
Copy code
python data_cleaning.py
This will clean the data and save it as cleaned_titanic.csv.

Part 2: Model Building
Navigate to the Part2_Model_Building folder.

Run the script:

bash
Copy code
python model_building.py
This will train the model and display evaluation metrics.

Part 3: Model Saving and Loading
Navigate to the Part3_Model_IO folder.

Run the script:

bash
Copy code
python model_io.py
This will save and load the model using joblib.

Part 4: FastAPI Endpoint for the Model
Navigate to the Part4_API folder.

Start the FastAPI server:

bash
Copy code
uvicorn api:app --reload
The server will start at http://127.0.0.1:8000.

You can access the prediction endpoint via a POST request at http://127.0.0.1:8000/predict.

Part 5: Gradio Deployment and UI
Navigate to the Part5_Deployment folder.

Run the Gradio app:

bash
Copy code
python app.py
This will start the Gradio UI locally. To interact with the model, enter the relevant Titanic passenger details, and the app will return the survival prediction.

To deploy the UI on Hugging Face Spaces, follow the instructions for creating a Space and pushing your code to the platform.

Deployment
Backend: You can deploy the FastAPI backend on Hugging Face Spaces or any cloud provider.
Frontend: Use Gradio to create a simple UI and deploy it on Hugging Face Spaces.
Files
data_cleaning.py: Script to clean and preprocess the Titanic dataset.
model_building.py: Script to build, train, and evaluate the machine learning model.
model_io.py: Script to save and load the trained model using joblib.
api.py: FastAPI application for serving the trained model.
app.py: Gradio-based user interface for interacting with the deployed model.
Author
Bilal Akhtar
Feel free to reach out if you have any questions or feedback!
