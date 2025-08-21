import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import yaml
from dvclive import Live   # ✅ new way

def main():
    # Load params
    params = yaml.safe_load(open("params.yaml"))
    lr = params["learning_rate"]

    df = pd.read_csv("data/processed/processed.csv")
    X = df[["feature1", "feature2"]]
    y = df["label"]

    model = LogisticRegression(C=1.0, solver="liblinear")
    model.fit(X, y)

    # Save model
    joblib.dump(model, "model.pkl")

    # ✅ Use Live object
    with Live() as live:
        live.log_param("learning_rate", lr)
        live.log_param("n_estimators", params["n_estimators"])

    print("✅ Model trained and params logged with dvclive")

if __name__ == "__main__":
    main()
