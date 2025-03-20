import sys
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    print("Original data shape:", df.shape)
    
    # Print missing values per column before cleaning
    print("Missing values per column before cleaning:")
    print(df.isna().sum())
    
    # Remove the extra column if it exists
    if "Unnamed: 32" in df.columns:
        df.drop("Unnamed: 32", axis=1, inplace=True)
        print("Dropped 'Unnamed: 32' column. New shape:", df.shape)
    
    # Apply label encoding to the 'diagnosis' column if it exists
    if "diagnosis" in df.columns:
        le = LabelEncoder()
        df["diagnosis"] = le.fit_transform(df["diagnosis"])
        print("Applied label encoding to 'diagnosis' column.")
    
    # Fill missing values for numeric columns only
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    print("Data shape after filling missing values:", df.shape)
    print("Missing values per column after cleaning:")
    print(df.isna().sum())

    # Save cleaned dataset
    df.to_csv("/home/doc-bd-a1/res_dpre.csv", index=False)
    print("Saved preprocessed dataset to res_dpre.csv")

    # Call next step in the pipeline
    import os
    os.system("python3 eda.py /home/doc-bd-a1/res_dpre.csv")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 dpre.py <dataset-path>")
    else:
        preprocess_data(sys.argv[1])

