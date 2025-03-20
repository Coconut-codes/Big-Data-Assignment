FROM ubuntu:latest

# Set noninteractive mode for apt-get to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Update and install required packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python3 -m venv /home/venv

# Activate virtual environment and install Python libraries
RUN /home/venv/bin/pip install --no-cache-dir \
    pandas \
    numpy \
    seaborn \
    matplotlib \
    scikit-learn \
    scipy

# Create a directory inside the container
RUN mkdir -p /home/doc-bd-a1/

# Copy dataset file to the container (Assuming dataset file exists in the build context)
COPY data.csv /home/doc-bd-a1/

# Set working directory
WORKDIR /home/doc-bd-a1/

# Open bash shell upon container startup with virtual environment activated
CMD ["/bin/bash", "-c", "source /home/venv/bin/activate && exec bash"]