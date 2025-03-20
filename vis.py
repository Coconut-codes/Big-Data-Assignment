import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize(file_path):
    df = pd.read_csv(file_path)
    
    # Choose the column to plot: use "radius_mean" if available,
    # otherwise, select the first numeric column (excluding 'id' and 'diagnosis' if possible)
    if "radius_mean" in df.columns:
        column_to_plot = "radius_mean"
        title = "Distribution of Radius Mean"
    else:
        # Exclude known non-numeric columns if present
        cols_to_exclude = {"id", "diagnosis"}
        numeric_cols = [col for col in df.select_dtypes(include=["number"]).columns if col not in cols_to_exclude]
        if numeric_cols:
            column_to_plot = numeric_cols[0]
            title = f"Distribution of {column_to_plot}"
        else:
            print("No numeric columns available for plotting.")
            return

    plt.figure(figsize=(8,6))
    sns.histplot(df[column_to_plot], kde=True)
    plt.title(title)
    plt.xlabel(column_to_plot)
    plt.ylabel("Frequency")
    plt.savefig("/home/doc-bd-a1/vis.png")
    
    print("Visualization saved as vis.png")

    # Call the next step in the pipeline
    import os
    os.system("python3 model.py /home/doc-bd-a1/res_dpre.csv")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 vis.py <dataset-path>")
    else:
        visualize(sys.argv[1])
