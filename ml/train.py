import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os
from airflow.utils.log.logging_mixin import LoggingMixin

log = LoggingMixin().log



def train_model(data_path, model_path):
    # Load dataset
    df = pd.read_csv(data_path)

    # Features and target
    X = df.drop(columns=["target"])
    y = df["target"]

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Save model
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    log.info(f"✅ Model trained and saved to {model_path}")

if __name__ == "__main__":
    train_model("data/housing.csv", "ml/model.pkl")