import sys
import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
    df.to_csv("/home/doc-bd-a1/data.csv", index=False)  # Pass this to next step
    print("Saved cleaned dataset to data.csv")
    
    # Call next step in pipeline
    import os
    os.system("python3 dpre.py /home/doc-bd-a1/data.csv")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 load.py <dataset-path>")
    else:
        load_data(sys.argv[1])
