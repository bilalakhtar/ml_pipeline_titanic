import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def clean_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Handle missing values
    df['Age'].fillna(df['Age'].median(), inplace=True)  # Fill missing ages with the median
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)  # Fill missing embarked with the mode
    df.drop(['Cabin', 'Ticket', 'Name'], axis=1, inplace=True)  # Drop less useful columns
    
    # Encode categorical variables
    label_encoder = LabelEncoder()
    df['Sex'] = label_encoder.fit_transform(df['Sex'])  # Encode 'Sex' column
    df['Embarked'] = label_encoder.fit_transform(df['Embarked'])  # Encode 'Embarked' column
    
    # Standardize the data
    scaler = StandardScaler()
    numeric_cols = ['Age', 'Fare', 'Parch', 'SibSp']
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    # Save cleaned data to CSV
    df.to_csv('Part1_Data_Cleaning/cleaned_titanic.csv', index=False)
    print("Data cleaning completed and saved to 'cleaned_titanic.csv'.")

if __name__ == "__main__":
    clean_data('titanic.csv')
