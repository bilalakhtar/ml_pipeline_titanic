# ml_pipeline_titanic
# Project: Titanic Survival Prediction Pipeline

This project builds a complete machine learning pipeline to predict the survival of Titanic passengers.

## Prerequisites
- Python 3.7+
- Required Libraries: pandas, scikit-learn, joblib, fastapi, uvicorn, gradio, ngrok

## Steps to Run

### Part 1: Data Cleaning
1. Navigate to the Part1_Data_Cleaning folder.
2. Run the script:
    
    ```bash
    python data_cleaning.py
    ```

   This will clean the data and save it as `cleaned_titanic.csv`.

### Part 2: Model Building
1. Navigate to the Part2_Model_Building folder.
2. Run the script:
    
    ```bash
    python model_building.py
    ```

   This will train the model and display evaluation metrics.

### Part 3: Model Saving and Loading
1. Navigate to the Part3_Model_IO folder.
2. Run the script:
    
    ```bash
    python model_io.py
    ```

   This will save and load the model using joblib.

### Part 4: FastAPI Endpoint for the Model
1. Navigate to the Part4_API folder.
2. Run the FastAPI server:
    
    ```bash
    uvicorn api:app --reload
    ```

   The server will start at `http://127.0.0.1:8000`.

### Part 5: Deployment with Gradio
1. Navigate to the Part5_Deployment folder.
2. Run the Gradio app:
    
    ```bash
    python app.py
    ```

3. Follow instructions to deploy the UI on Hugging Face Spaces.

## Deployment
- Deploy the FastAPI backend on Hugging Face Spaces.
- Deploy the Gradio UI on Hugging Face Spaces.


- data_cleaning.py: Script to clean and preprocess the Titanic dataset.
- model_building.py: Script to build, train, and evaluate the machine learning model.
- model_io.py: Script to save and load the trained model using joblib.
- api.py: FastAPI application for serving the trained model.
- app.py: Gradio-based user interface for interacting with the deployed model.

Author
Bilal Akhtar
Feel free to reach out if you have any questions or feedback!
