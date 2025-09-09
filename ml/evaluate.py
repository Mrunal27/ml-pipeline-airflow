import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error
from airflow.utils.log.logging_mixin import LoggingMixin
log = LoggingMixin().log



def evaluate_model(data_path, model_path):
    # Load dataset
    df = pd.read_csv(data_path)

    # Features and target
    X = df.drop(columns=["target"])
    y = df["target"]

    # Load model
    model = joblib.load(model_path)

    # Predict and evaluate
    predictions = model.predict(X)
    mse = mean_squared_error(y, predictions)
    log.info(f"📊 Mean Squared Error: {mse:.2f}")

if __name__ == "__main__":
    evaluate_model("data/housing.csv", "ml/model.pkl")