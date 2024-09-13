import joblib

def save_model(model, file_path):
    joblib.dump(model, file_path)
    print(f"Model saved to {file_path}")

def load_model(file_path):
    model = joblib.load(file_path)
    print(f"Model loaded from {file_path}")
    return model

if __name__ == "__main__":
    from Part2_Model_Building.model_building import build_and_evaluate_model
    model = build_and_evaluate_model('Part1_Data_Cleaning/cleaned_titanic.csv')
    save_model(model, 'Part3_Model_IO/model.pkl')
    loaded_model = load_model('Part3_Model_IO/model.pkl')
