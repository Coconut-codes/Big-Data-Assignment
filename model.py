import sys
import pandas as pd
from sklearn.cluster import KMeans

def cluster_data(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Remove the extra column if it exists
    if "Unnamed: 32" in df.columns:
        df.drop("Unnamed: 32", axis=1, inplace=True)
    
    # Drop non-numeric columns that are not useful for clustering (e.g., 'id' and 'diagnosis')
    if "id" in df.columns and "diagnosis" in df.columns:
        df_numeric = df.drop(["id", "diagnosis"], axis=1)
    else:
        # Fallback: select only numeric columns
        df_numeric = df.select_dtypes(include=['number'])
    
    # Optional: print shape to verify the data used for clustering
    print("Shape of numeric data for clustering:", df_numeric.shape)
    
    # Create and fit the KMeans model using numeric features
    model = KMeans(n_clusters=3, random_state=42, n_init=10)
    clusters = model.fit_predict(df_numeric)
    
    # Add the cluster labels to the original DataFrame
    df["Cluster"] = clusters

    # Get the count of records in each cluster and save to a text file
    cluster_counts = df["Cluster"].value_counts().to_string()
    with open("/home/doc-bd-a1/k.txt", "w") as f:
        f.write(cluster_counts)

    print("K-means clustering results saved in k.txt")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 model.py <dataset-path>")
    else:
        cluster_data(sys.argv[1])

