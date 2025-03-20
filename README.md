**Team members**

**Ahmed Gomaa Moftah 202001501**

**NourElhoda Medhat 202001846**

**Jana Amer Mohamed 211001627**

**Wisconsin Breast Cancer Clustering Project**

` `**Overview of the assignment:**

This assignemnt applies data preprocessing, exploratory data analysis (EDA), visualization, and K-Means clustering to the Wisconsin Breast Cancer dataset. The goal is to clean the dataset, visualize patterns, and apply clustering on cancer data. Docker is used to containerize the project for reproducibility.


Directory Structure

project-folder/

│── Dockerfile

│── requirements.txt

│── data/

│   ├── data.csv   Raw dataset

│── scripts/

│   ├── dpre.py    Data Preprocessing

│   ├── eda.py     Exploratory Data Analysis

│   ├── vis.py    Data Visualization

│   ├── model.py   Clustering Model

│── results/

│   ├── res\_dpre.csv   Processed data

│   ├── vis.png        Visualization output

│   ├── k.txt         Clustering results

│── README.md         Documentation

│── run.sh             Shell script for execution


` `Installation & Setup

1\. Install Docker (if not installed)

bash

sudo apt-get update

sudo apt-get install docker.io -y


2\. Clone or Set Up the Project

bash

git clone <your-repo-url>

cd project-folder


3\. Create a Virtual Environment 

bash

python3 -m venv venv

venv\Scripts\activate  

pip install -r requirements.txt



Dockerizing the Project

Dockerfile

dockerfile

Use official Python image

FROM python:3.12

` `Set the working directory

WORKDIR /home/doc-bd-a1

` `Copy project files

COPY . /home/doc-bd-a1

` `Install dependencies

RUN pip install --no-cache-dir -r requirements.txt

Run the preprocessing script when the container starts

CMD ["python3", "scripts/dpre.py", "data/data.csv"]


` `Build the Docker Image

bash

docker build -t breast-cancer-project .

` `Run the Docker Container

bash

docker run --rm -v $(pwd)/results:/home/doc-bd-a1/results breast-cancer-project

This runs the pipeline inside Docker and \*\*mounts the results\*\* folder to access outputs.


**Execution Pipeline**

` `**Step 1: Preprocessing**

bash

python3 scripts/dpre.py data/data.csv

Processes:

\- Drops unnecessary columns.

\- Handles missing values.

\- Encodes categorical variables (`diagnosis` → 1 for \*\*Malignant\*\*, 0 for \*\*Benign\*\*).

\- Saves the processed dataset (`res\_dpre.csv`).

**Step 2: Exploratory Data Analysis (EDA)**

bash

python3 scripts/eda.py results/res\_dpre.csv

\- Saves insights as `eda-in-1.txt`, `eda-in-2.txt`, etc.

` `**Step 3: Visualization**

bash

python3 scripts/vis.py results/res\_dpre.csv

\- Generates ‘vis.png’.

` `**Step 4: Clustering**

bash

python3 scripts/model.py results/res\_dpre.csv

\- Runs K-Means clustering.

\- Saves cluster assignments in `k.txt`.

**Automating Execution**

Creation of  a “run.sh” script to automate everything:

bash

#!/bin/bash

python3 scripts/dpre.py data/data.csv

python3 scripts/eda.py results/res\_dpre.csv

python3 scripts/vis.py results/res\_dpre.csv

python3 scripts/model.py results/res\_dpre.csv

Run it with:

bash

chmod +x run.sh

./run.sh

Errors:

Error 1:

Your issue is caused by PEP 668, which prevents system-wide pip installations in Ubuntu

22\.04+ due to it being an externally managed Python environment.

Solution: Use a Virtual Environment

Modify your Dockerfile to install Python packages inside a virtual environment:

Updated Dockerfile

I'll modify your existing Dockerfile to:

1\. Install python3-venv.

2\. Create a virtual environment at /home/venv.

3\. Install required Python libraries inside the virtual environment.

4\. Use this virtual environment when running Python.

Error 2:

The diagnosis feature data type was non numerical (categorical), and we converted it to numerical.

Error 3:

Nano command was not working, so we must install it to work with this command

apt-get update && apt-get install -y nano


Outputs & Results

‘res\_dpre.csv’ :  Preprocessed dataset 

‘eda-in-1.txt’ :  EDA insights 

‘vis.png’ :      Visualization output 

‘k.txt’ :        Clustering results 


**Coconut-codes**- [https://github.com/Coconut-codes/Big-Data-Assignment.git]
