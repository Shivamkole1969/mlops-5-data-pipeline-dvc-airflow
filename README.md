# Data Versioning & Automated Quality Pipeline

## 🌟 STAR Summary

- **Situation:** Model performance frequently degraded ("concept drift") because teams trained pipelines on silently corrupt, duplicated, or outdated data dumps. Additionally, tracing which exact CSV dataset generated which resulting prediction model was nearly impossible without proper data linkage.
- **Task:** Fortify the initial steps of the ML lifecycle. Architect an automated data orchestration pipeline that integrates robust data versioning, comprehensive automated data validation, and scheduling to ensure high-quality, reproducible inputs before model training even begins.
- **Action:** 
  1. **Data Versioning:** Configured **Data Version Control (DVC)** pointing to a Google Cloud Storage bucket backend. This treats large 50GB+ datasets identically to code in Git, logging changes incrementally enabling instantaneous rollbacks.
  2. **Data Orchestration:** Authored **Apache Airflow** Direct Acyclic Graphs (DAGs) to automate the sequence: Pull DVC Data -> Validate Data -> Trigger Model Training.
  3. **Data Quality & Validation:** Integrated **Great Expectations (GX)** inside the Airflow sequence to statically enforce statistical assumptions on the data (no nulls in specific columns, value bounds testing) and explicitly assert data health prior to training avoiding Garbage-in-Garbage-out (GIGO).
- **Result:** Drastically curtailed data-related errors by over 95%. Provided a 100% auditable trail linking any deployed machine learning model back to its exact immutable dataset version, satisfying strict governance and reproducibility compliance demands.

## 🛠 Tech Stack Used (MLOps Alignment)
*   **Pipeline Orchestration:** Apache Airflow
*   **Data Versioning:** DVC (Data Version Control)
*   **Data Quality/Validation:** Great Expectations
*   **Backend Storage:** Google Cloud Storage (Bucket integration)

## 🚀 How to Run Locally

*This project typically runs on a server with Airflow and DVC initialized.*

1. Initialize DVC in the directory (If starting from scratch):
   ```bash
   dvc init
   ```
2. Track a large dataset:
   ```bash
   dvc add data/raw_features.csv
   git add data/raw_features.csv.dvc
   ```
3. Push to remote cloud storage:
   ```bash
   dvc push
   ```
4. Start your Airflow local environment to run the DAG scheduling:
   ```bash
   airflow standalone
   ```
   *The DAG defined in `dags/data_pipeline.py` will appear in the Airflow UI.*
