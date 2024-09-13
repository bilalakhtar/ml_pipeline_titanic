import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

def build_and_evaluate_model(file_path):
    # Load cleaned data
    df = pd.read_csv(file_path)
    
    # Split data into features and target
    X = df.drop('Survived', axis=1)  # 'Survived' is the target column
    y = df['Survived']
    
    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Choose a model
    model = RandomForestClassifier(random_state=42)
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    
    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")

    return model

if __name__ == "__main__":
    model = build_and_evaluate_model('Part1_Data_Cleaning/cleaned_titanic.csv')
