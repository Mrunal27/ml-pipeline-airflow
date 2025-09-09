# 🧠 ML Pipeline Orchestrated with Airflow & Docker

This project demonstrates a modular machine learning pipeline orchestrated using Apache Airflow and Docker. It includes data preparation, model training, and evaluation—all wrapped in a reproducible, containerized workflow.

## 🚀 Project Overview

- **Pipeline Tasks**:
  - `prepare_dataset.py`: Loads and preprocesses housing data
  - `train.py`: Trains a regression model and saves it as `model.pkl`
  - `evaluate.py`: Computes evaluation metrics (e.g., MSE) on the trained model

- **Orchestration**:
  - Airflow DAG (`ml_pipeline_dag.py`) defines task dependencies
  - Uses `PythonOperator` for modular execution
  - DAG structure: `prepare_dataset → train_model → evaluate_model`

- **Infrastructure**:
  - Dockerized Airflow 3.x setup
  - PostgreSQL and Redis services
  - `.env` file for UID/GID mapping (Windows compatibility)

## 🧰 Tech Stack

| Layer           | Tools Used               |
|----------------|--------------------------|
| Orchestration  | Apache Airflow           |
| Containerization| Docker, docker-compose   |
| ML Framework   | Scikit-learn, Pandas     |
| Language       | Python                   |
