# Start from the official Airflow image
FROM apache/airflow:3.0.0

# Switch to root to install additional system dependencies (if needed)
USER root

# Install any system-level dependencies your Python libs might require (optional)
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libpq-dev \
#     && rm -rf /var/lib/apt/lists/*

# Switch back to airflow user
USER airflow

# Copy requirements.txt into the container
COPY requirements.txt /requirements.txt

# Install python dependencies
RUN pip install --no-cache-dir -r /requirements.txt
