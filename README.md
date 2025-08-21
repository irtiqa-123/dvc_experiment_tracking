
# 🧪 DVC Experiment Tracking (with Local Storage)

This is a **simple ML pipeline project** demonstrating how to use  
**DVC (Data Version Control)** with **local remote storage** to track:

- 📂 Data (raw & processed)
- ⚙️ Pipelines (ingestion → preprocessing → training)
- 📊 Experiments (with different hyperparameters)
- 💾 Local storage as a remote backend

---

## 📂 Project Structure

dvc_experiment_tracking/
├── data/
│ ├── raw/
│ │ └── data.csv
│ └── processed/
├── src/
│ ├── ingest.py
│ ├── preprocess.py
│ └── train.py
├── dvc.yaml
├── params.yaml
├── template.py
└── README.md


---

## 🚀 Setup Instructions

1️⃣ **Clone the repo & install dependencies**  

```bash
git clone <your_repo_url>
cd dvc_experiment_tracking
pip install -r requirements.txt


2️⃣ Initialize DVC & local remote storage

dvc init
mkdir ../dvc_storage
dvc remote add -d local_remote ../dvc_storage

⚙️ Running the Pipeline

Reproduce the full pipeline:

dvc repro


This will execute:

ingestion → load data

preprocessing → clean data

training → train & save model (model.pkl)

💾 Pushing Data/Models to Local Storage

After running pipeline:

dvc push


This saves all tracked files into ../dvc_storage.

To restore if deleted:

dvc pull

🧪 Running Experiments

Change hyperparameters in params.yaml:

learning_rate: 0.01
n_estimators: 100


Run a new experiment:

dvc exp run


Compare experiments:

dvc exp show


Example output:

Experiment     Created    Accuracy   learning_rate   n_estimators
workspace      -          0.60       0.01            100
main           07:06 PM   -          -               -
exp-1234       07:18 PM   0.62       0.05            200

📊 Tracking Metrics with DVCLive

We use DVCLive to log metrics during training.
After experiments, metrics are stored in:

dvclive/metrics.json

🎯 Key Learnings

✅ Use DVC for versioning datasets & models

✅ Push artifacts into local remote storage (../dvc_storage)

✅ Track experiments with dvc exp run & compare with dvc exp show

✅ Reproduce pipelines anytime using dvc repro

🤝 Contributing

Feel free to fork, create issues, or submit pull requests 🚀

📝 License

MIT License © 2025  


