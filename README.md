# Airflow Reddit Data Engineering Project

This project demonstrates a **data engineering pipeline** using **Apache Airflow** to extract, transform, and store data from **Reddit**. The pipeline is fully Dockerized for easy setup and execution.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Architecture](#architecture)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Running the Pipeline](#running-the-pipeline)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Project Overview

The Airflow Reddit project automates the collection of Reddit posts and stores them for analysis. This includes:

- Pulling posts from specific subreddits via **Reddit API**  
- Transforming the data into **CSV format**  
- Storing the CSV files in a local `data/` folder (can be configured to S3)  
- Orchestrating all tasks using **Airflow DAGs**  

---

## Features

- Fully **Dockerized** environment with Airflow  
- Configurable **subreddits** and **time intervals**  
- Automated **ETL workflow** with Airflow DAGs  
- CSV storage for easy analysis  
- Ready to scale to cloud storage like **AWS S3**  

---

## Architecture


- **Extractor:** Pulls Reddit posts via PRAW API  
- **Transformer:** Cleans and formats data  
- **Loader:** Stores results as CSV files in `data/` folder  
- **Scheduler:** Airflow manages the DAG execution  

---

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started)  
- [Docker Compose](https://docs.docker.com/compose/install/)  
- Reddit API credentials:  
  - Client ID  
  - Client Secret  
  - User Agent  

---

### Installation

1. Clone the repository:

```bash
git clone https://github.com/karthik-bommineni/reddit-airflow-data-engineering.git
cd reddit-airflow-data-engineering
```
2. Create a .env file in the project root with your Reddit API credentials:

   ```bash
   REDDIT_CLIENT_ID=<your-client-id>
   REDDIT_CLIENT_SECRET=<your-client-secret>
   REDDIT_USER_AGENT=<your-user-agent>
   ```

3. Build and start the docker containers: (Make sure you enter in your AWS Access key and the AWS Secret key in the correct fields in docker-compose.yaml file)

   ```bash
   docker-compose up --build -d
   ```

4. Access the Airflow UI at http://localhost:8080

Default credentials:

Username: airflow

Password: airflow
