import pandas as pd
import joblib
from sklearn.metrics import accuracy_score
from dvclive import Live   # ✅ new way

def main():
    model = joblib.load("model.pkl")
    df = pd.read_csv("data/processed/processed.csv")
    X = df[["feature1", "feature2"]]
    y = df["label"]

    preds = model.predict(X)
    acc = accuracy_score(y, preds)

    # ✅ Use Live object
    with Live() as live:
        live.log_metric("accuracy", acc)

    # Also save metrics.txt for DVC
    with open("metrics.txt", "w") as f:
        f.write(f"Accuracy: {acc}\n")

    print(f"✅ Evaluation done! Accuracy: {acc}")

if __name__ == "__main__":
    main()
