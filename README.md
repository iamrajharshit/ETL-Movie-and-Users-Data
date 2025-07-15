# 🎬 ETL Pipeline with Apache Airflow

This project implements an automated **ETL (Extract, Transform, Load)** pipeline using **Apache Airflow** to process **movie and user datasets**. The pipeline is designed to run on a scheduled basis and is fully orchestrated using Airflow DAGs.

---

## 🚀 Features

- ✅ Extraction of raw movie and user data (CSV or API supported)
- 🔄 Transformation of data (cleaning, filtering, formatting)
- 📦 Loading into a data warehouse or database (e.g., PostgreSQL, SQLite)
- 🕓 Scheduled execution using Airflow DAGs
- 📊 Monitoring and logging of each task in the pipeline

---

## 🛠️ Tech Stack

- **Apache Airflow** – Workflow orchestration
- **Python** – Data processing
- **Pandas** – Data transformation
- **SQLAlchemy / PostgreSQL / SQLite** – Database support
- **Docker (Optional)** – For containerized deployment

---

## 📁 Project Structure
```
etl-airflow/
│
├── dags/
│ └── etl_pipeline.py # Main Airflow DAG definition
│
├── data/
│ └── movies.csv # Sample movie data
│ └── users.csv # Sample user data
│
├── scripts/
│ └── extract.py # Extraction logic
│ └── transform.py # Transformation logic
│ └── load.py # Loading logic
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation

```
