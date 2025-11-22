
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

def train():
    df = pd.read_csv("sample_data.csv")
    X = df[["age","months_active","avg_monthly_spend","support_tickets"]]
    y = df["churn"]

    model = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression())
    ])

    model.fit(X, y)
    joblib.dump(model, "model.pkl")

if __name__ == "__main__":
    train()
