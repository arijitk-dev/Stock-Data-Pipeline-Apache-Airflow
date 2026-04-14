# 📊 Stock Data Pipeline using Apache Airflow

## 🚀 Overview

This project implements an end-to-end **data pipeline** using **Apache Airflow** to process stock market data incrementally.

The pipeline simulates a real-world batch processing system where data is:

- Ingested in chunks (window-based processing)
- Cleaned and validated
- Analyzed for key insights
- Exported in a structured format

---

## 🧠 Pipeline Architecture

```
Extract → Transform → Analyze → Export
```

Each stage is implemented as an independent task and orchestrated using Apache Airflow.

---

## 📂 Project Structure

```
project/
│
├── dags/
│   ├── stock_pipeline_dag.py
│   ├── extract.py
│   ├── transform.py
│   ├── analyze.py
│   └── export.py
│
├── data/
│   └── Mastercard_stock.csv
│
├── output/
│   ├── raw.csv
│   ├── clean.csv
│   ├── result.csv
│   └── results/
│
└── offset tracking via Airflow Variable
```

---

## ⚙️ Technologies Used

- Python 3.11
- Apache Airflow (v3.2.0)
- Pandas
- CSV processing

---

## 🔄 Pipeline Stages

### 🔹 Stage 1: Data Understanding

- Identified dataset structure and schema
- Verified dataset location
- Confirmed Airflow environment setup

---

### 🔹 Stage 2: Incremental Data Ingestion

- Reads data from CSV using a **window-based approach**
- Tracks processed rows using **Airflow Variables (offset)**
- Ensures only new data is processed in each run

---

### 🔹 Stage 3: Data Cleaning & Validation

- Removes whitespace
- Converts `Date` to datetime
- Validates numeric columns
- Filters invalid records (nulls, negative values)

---

### 🔹 Stage 4: Analytical Processing

- Identifies:
  - Highest stock price (`High`)
  - Lowest stock price (`Low`)

- Captures corresponding row details

---

### 🔹 Stage 5: Result Export

- Outputs structured CSV with schema:

```
type, date, open, high_or_low, close, volume
```

- File name dynamically generated using date range

---

## ▶️ How to Run the Project

### 1️⃣ Activate Virtual Environment

```bash
source airflow_env/bin/activate
```

---

### 2️⃣ Install Dependencies

```bash
pip install pandas
```

---

### 3️⃣ Start Airflow

```bash
airflow standalone
```

---

### 4️⃣ Access Airflow UI

```
http://localhost:8080
```

---

### 5️⃣ Add DAG Files

Copy all pipeline files into:

```
~/airflow/dags/
```

---

### 6️⃣ Run Pipeline

- Enable DAG in UI
- Click **Trigger DAG**

---

## 📊 Output Example

```
type,date,open,high_or_low,close,volume
highest,2023-02-10,1200,1500,1480,100000
lowest,2023-01-05,900,850,870,80000
```

---

## ∆ Image
<img width="1440" height="758" alt="Screenshot 2026-04-14 at 4 12 56 PM" src="https://github.com/user-attachments/assets/da96973f-f70a-4622-a039-02446f43d88f" />


## ⚠️ Important Notes

- Airflow Variables must store values as **strings**
- File paths must be **absolute paths**
- All scripts must be inside the `dags/` folder

---

## 💡 Key Features

- Incremental processing using offset tracking
- Modular ETL design
- Airflow-based orchestration
- Clean and validated data pipeline
- Dynamic output generation

---

## 🚀 Future Enhancements

- Add logging and monitoring
- Integrate with cloud storage (AWS S3)
- Implement retry and failure handling
- Extend to real-time streaming (Kafka)

---

## 🧑‍💻 Author

**Arijit Kumar Sahu**

---

## 📌 Conclusion

This project demonstrates how to build a scalable and modular data pipeline using Apache Airflow, simulating real-world data engineering workflows with incremental data processing and structured output generation.
