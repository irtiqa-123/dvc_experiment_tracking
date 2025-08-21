# Data preprocessing script
import pandas as pd

def main():
    df = pd.read_csv("data/raw/data.csv")
    # Simple normalization
    df["feature1"] = df["feature1"] / df["feature1"].max()
    df["feature2"] = df["feature2"] / df["feature2"].max()
    df.to_csv("data/processed/processed.csv", index=False)
    print("✅ Processed data saved at data/processed/processed.csv")

if __name__ == "__main__":
    main()
