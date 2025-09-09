# 🧠 Modular ML Pipeline with Airflow & Docker

This project demonstrates a reproducible machine learning pipeline orchestrated using Apache Airflow and Docker. It includes modular tasks for data preparation, model training, and evaluation—designed to reflect scalable backend workflows and infrastructure reliability.

---

## 🚀 Pipeline Overview

This ML pipeline automates the following stages:

- **Data Preparation** (`prepare_dataset.py`)  
  Loads and preprocesses housing data for training.

- **Model Training** (`train.py`)  
  Trains a regression model using scikit-learn and saves it as `model.pkl`.

- **Model Evaluation** (`evaluate.py`)  
  Computes evaluation metrics (e.g., Mean Squared Error) on the trained model.

The pipeline is orchestrated via an Airflow DAG (`ml_pipeline_dag.py`) using `PythonOperator`, with the following task flow:

```text
[prepare_dataset] → [train_model] → [evaluate_model]

## 🧰 Tech Stack

| Layer            | Tools Used               |
|------------------|--------------------------|
| Orchestration    | Apache Airflow           |
| Containerization | Docker, docker-compose   |
| ML Framework     | Scikit-learn, Pandas     |
| Language         | Python                   |

🛠️ Infrastructure Details
- Airflow 3.x deployed via Docker Compose
- PostgreSQL & Redis services for metadata and caching
- .env file for UID/GID mapping (Windows compatibility)

📦 Setup Instructions
Clone the repo and launch the pipeline:

git clone https://github.com/yourusername/ml-airflow-pipeline.git
cd ml-airflow-pipeline
docker-compose up --build

📈 Sample Output
- Trained model saved as model.pkl
- Evaluation metrics printed in logs (e.g., MSE: 0.032)
- DAG visualized in Airflow UI with task status tracking

🔍 Reliability & Validation
- Modular task design for reproducibility and testability
- Dockerized environment ensures consistent execution
- Logging and output validation built into each stage
- .env integration for cross-platform compatibility

💡 Why This Project?
This pipeline was built to showcase backend orchestration and infrastructure skills as part of my pivot from SDET into ML Infra and platform engineering. It reflects my focus on modular design, reproducible workflows, and system reliability.

🔭 Future Enhancements
- Add CI/CD integration with GitHub Actions
- Integrate model registry (e.g., MLflow)
- Wrap model inference in FastAPI for API deployment
- Add unit tests and DAG-level validation hooks

👤 Author
Mrunal

📄 License
This project is licensed under the MIT License.

---
_#MachineLearning #Airflow #Docker #BackendEngineering #CareerPivot #OpenToWork_
