import joblib

def save_model(model, file_path):
    joblib.dump(model, file_path)
    print(f"Model saved to {file_path}")

def load_model(file_path):
    model = joblib.load(file_path)
    print(f"Model loaded from {file_path}")
    return model

if __name__ == "__main__":
    model = build_and_evaluate_model('/content/drive/MyDrive/Colab Notebooks/cleaned_titanic.csv')
    save_model(model, '/content/drive/MyDrive/Colab Notebooks/model.pkl')
    loaded_model = load_model('/content/drive/MyDrive/Colab Notebooks/model.pkl')
