from sklearn.datasets import fetch_california_housing
import pandas as pd
import os


def prepare(output_path):
    # Load dataset
    data = fetch_california_housing()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target

    # Ensure data folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save to CSV
    df.to_csv(output_path, index=False)
    print(f"✅ Dataset saved to {output_path}")

if __name__ == "__main__":
    prepare("data/housing.csv")