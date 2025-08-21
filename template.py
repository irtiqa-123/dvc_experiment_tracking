import os

def create_project_structure():
    folders = [
        "data/raw",
        "data/processed",
        "src"
    ]
    files = {
        "src/data_ingestion.py": "# Data ingestion script\n",
        "src/data_preprocessing.py": "# Data preprocessing script\n",
        "src/train.py": "# Training script\n",
        "src/evaluate.py": "# Evaluation script\n",
        "params.yaml": "learning_rate: 0.01\nn_estimators: 100\n",
        "requirements.txt": "pandas\nscikit-learn\ndvc\n",
        "README.md": "# Easy DVC Project\n"
    }

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    for filepath, content in files.items():
        with open(filepath, "w") as f:
            f.write(content)

    print("✅ Project structure created!")

if __name__ == "__main__":
    create_project_structure()
