# Data ingestion script
import pandas as pd

def main():
    # Tiny dataset (2 features + label)
    data = {
        "feature1": [1, 2, 3, 4, 5],
        "feature2": [5, 4, 3, 2, 1],
        "label": [1, 0, 1, 0, 1]
    }
    df = pd.DataFrame(data)
    df.to_csv("data/raw/data.csv", index=False)
    print("✅ Data saved at data/raw/data.csv")

if __name__ == "__main__":
    main()
