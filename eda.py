import sys
import pandas as pd

def eda(file_path):
    df = pd.read_csv(file_path)

    # Insight 1: Dataset shape
    shape_insight = f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns."

    # Insight 2: Missing values per column
    missing_insight = f"Missing values per column:\n{df.isnull().sum()}"

    # Insight 3: Summary statistics for numeric features
    summary_insight = f"Summary statistics for numeric features:\n{df.describe()}"

    # Insight 4: Diagnosis distribution (assuming label encoding has been applied in dpre.py)
    if "diagnosis" in df.columns:
        diagnosis_counts = df["diagnosis"].value_counts()
        diagnosis_insight = f"Diagnosis distribution (encoded):\n{diagnosis_counts}"
    else:
        diagnosis_insight = "No 'diagnosis' column found."

    insights = [
        shape_insight,
        missing_insight,
        summary_insight,
        diagnosis_insight
    ]

    for i, insight in enumerate(insights, 1):
        with open(f"/home/doc-bd-a1/eda-in-{i}.txt", "w") as f:
            f.write(insight)

    print("EDA insights saved as eda-in-1.txt, eda-in-2.txt, ...")

    # Call the next step in the pipeline
    import os
    os.system("python3 vis.py /home/doc-bd-a1/res_dpre.csv")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 eda.py <dataset-path>")
    else:
        eda(sys.argv[1])

