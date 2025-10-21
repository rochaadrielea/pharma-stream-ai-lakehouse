## Pharma Stream AI Lakehouse
Pharmaceutical companies receive millions of reviews, complaints, lab reports, and photos every year — from patients, doctors, and regulators.
Most of that data is unstructured (text, PDFs, images, scanned leaflets) and spread across different departments like marketing, quality, and safety teams.

This means:

* Product issues (like side effects or packaging defects) go unnoticed for weeks or months.

* Compliance teams must manually analyze documents — slow and error-prone.

* Leadership has no real-time visibility into patient sentiment or product perception.

So, this is a tool to turn chaos into clarity.
With this product there are 4 deliverables:

1️⃣ **Actionable, AI-generated insights**

LLM (Generative AI) creates concise product summaries, risk alerts, and marketing or operations recommendations based on live data.

Example: “Product A is trending negatively due to packaging complaints”

2️⃣ **Automated Review Understanding (NLP)**

Uses NLP (DistilBERT + topic modeling) to clean and analyze thousands of daily reviews and reports, extracting sentiment, key themes, and frequent complaints.
As result, Replaces manual reading with automatic trend detection, saving hundreds of analyst hours per month.

Example: “Top complaint keywords this week: ‘broken seal,’ ‘delayed delivery,’ ‘wrong dosage label.’ Average customer sentiment fell from 4.1 to 3.5 stars.”

3️⃣ **Visual Intelligence (Computer Vision)**

Uses image models (ResNet50, ViT) and OCR to analyze photos of incoming and shelf products. Automatically detects packaging inconsistencies, missing dosage information, or altered warning labels — ensuring all items match approved references before being stocked or sold.
This Helps pharmacies verify authenticity, safety, and compliance of medicines at the point of sale — preventing counterfeit or mislabeled products from reaching customers, improving trust and operational safety.

Example:“AI detected a mismatch between the expected packaging of Paracetamol 500 mg and a newly delivered batch — missing the expiry date label. The item was automatically flagged for review before restocking.”

4️⃣ **Unified Lakehouse & BI Visibility**

Integrates all data into a Lakehouse (Bronze → Silver → Gold) and visualizes it in Power BI dashboards and REST APIs.
Gives all teams — from quality to leadership — a single, trusted view of product health, sentiment, and compliance.

Example: “Power BI dashboard shows live metrics: sentiment score per region, top complaints, flagged batches, and LLM insight feed, all updated every 5 minutes.”


This is a real-time, multimodal **AI & MLOps platform** designed to transform raw pharmaceutical reviews, images, and documents into explainable insights — using **Kafka, Spark, MinIO, MLflow, Airflow, and FastAPI** under a **Lakehouse architecture (Bronze → Silver → Gold)**.  

This project simulates how a modern pharmaceutical company could detect product issues, monitor sentiment, and ensure compliance using a unified data + AI pipeline built with open-source and cloud-ready components.

---

## 🎯 Project Overview

**Pharma Stream AI Lakehouse** demonstrates an end-to-end **data engineering + AI system** that:

* Streams live product reviews and visual data via **Kafka**  
* Stores raw events in **MinIO (Bronze)**  
* Processes data with **Spark Structured Streaming (Silver → Gold)**  
* Runs **Deep Learning models** for sentiment, topics, and image classification  
* Tracks ML experiments with **MLflow**  
* Orchestrates all tasks via **Airflow**  
* Serves explainable insights through **FastAPI** and **Streamlit**  
* Publishes final analytics to **Power BI** for executive reporting  

---

## 🧩 Current Architecture

Producers → Kafka → MinIO (Bronze) → Spark ETL → MLflow Tracking
↓
Airflow Scheduler (Nightly DAGs)
↓
FastAPI REST API + Streamlit App
↓
Power BI Executive Dashboard


---

## 🚀 Goals & Use Cases

| Goal | Description |
|------|--------------|
| 🧠 Real-time AI insights | Stream product reviews and detect issues early |
| 🧬 Multimodal analysis | Combine text (NLP), image (CV), and documents (OCR) |
| 🤖 Deep Learning integration | DistilBERT, ResNet, YOLO, and FLAN-T5 for summaries |
| 🔍 Explainable AI | Grad-CAM visual overlays + citation-based RAG summaries |
| 🛡️ Responsible AI | Bias detection, PII masking, confidence tagging |
| 📈 Executive view | Power BI dashboards on Gold Layer outputs |
| 🧰 MLOps workflow | MLflow + Airflow orchestration + Dockerized stack |

---

## 🧠 Core AI & ML Components

| Domain | Model / Technique | Purpose | Tracked in |
|--------|--------------------|----------|-------------|
| NLP | DistilBERT | Sentiment classification | MLflow |
| NLP | KeyBERT + YAKE | Keyphrase extraction | MLflow |
| NLP | BERTopic | Topic clustering | Airflow |
| CV | ResNet50 / ViT | Image classification (packshots) | MLflow |
| CV | EasyOCR + Tesseract | OCR text extraction | MLflow |
| CV | Grad-CAM | Visual explainability | Streamlit |
| CV | YOLOv8n | Icon detection (e.g., sugar-free, age 12+) | MLflow |
| RAG/LLM | FAISS + FLAN-T5 | Evidence-based product summaries | MongoDB |
| RAG/LLM | NLI Gate (MNLI) | Hallucination filter / [SPECULATIVE] flag | Airflow |
| Forecasting | Prophet / SARIMAX | Predict sentiment trends | Power BI |
| Anomaly | IsolationForest | Detect outlier spikes in feedback | Kafka Alerts |

---

## 🧱 Tech Stack

| Layer | Technology |
|-------|-------------|
| Streaming | Apache Kafka + Python client |
| Storage | MinIO (S3-compatible) |
| Processing | Apache Spark (Scala + PySpark) |
| Workflow | Apache Airflow |
| Experiment Tracking | MLflow |
| API | FastAPI + Prometheus metrics |
| UI | Streamlit + Power BI |
| Infra | Docker Compose + Terraform |
| NoSQL | MongoDB (RAG logs, bias reports) |

---


---

## 🧮 Project Stages & Progress

| Stage | Description | Status |
|--------|-------------|--------|
| **1. Infrastructure Setup** | Docker Compose stack (Kafka, Airflow, MLflow, MinIO) | ✅ Completed |
| **2. Kafka → MinIO Streaming** | Python producer + consumer writing to Bronze | ✅ Completed |
| **3. MLflow Tracking** | Configured tracking server + artifact storage | ✅ Completed |
| **4. Spark ETL to Silver** | Scala job transforming reviews to clean layer | 🔄 In progress |
| **5. Deep Learning Integration** | DistilBERT, ResNet, OCR | 🔄 In progress |
| **6. Airflow DAG Automation** | Nightly pipeline (ingest, summarize, forecast) | 🔄 In progress |
| **7. FastAPI REST Service** | Endpoints for sentiment/summaries | 🔄 In progress |
| **8. Streamlit Dashboard** | Interactive multimodal visualization | 🔄 In progress |
| **9. Power BI Executive Report** | Gold Layer integration | 🔜 Planned |
| **10. CI/CD & Terraform Cloud Deployment** | Reproducible infrastructure | 🔜 Planned |

---

## 📊 Example Outputs

- **Sentiment Trend:** Gold layer time series from Spark aggregation  
- **Visual Insights:** Grad-CAM overlays highlighting detected features  
- **Summaries:** RAG-based explanations with citations and confidence scores  
- **Forecasts:** Prophet-based prediction of positive/negative review ratios  
- **Bias Audit:** Airflow-generated report by language/category  

---

## 🛡️ Responsible & Secure AI

- 🔒 PII scrub and anonymization (names, emails, phones)
- 🧩 Bias detection and fairness report
- 📜 Audit trails in MongoDB (rag_logs, bias_reports)
- 🧠 Explainability (Grad-CAM, citations, confidence badges)
- ⚖️ GDPR/FADP alignment for synthetic data simulation

---

## 🧰 How to Run Locally

```bash
# 1. Start infrastructure
docker compose up -d

# 2. Produce sample reviews to Kafka
python src/stream/py_producer.py --topic reviews_raw --rate 1/s

# 3. Run Spark ETL job
spark-submit --class ReviewsStream --master local[4] target/scala-2.12/ReviewsStream-assembly.jar

# 4. Trigger Airflow DAG manually
airflow dags trigger pharma_nightly

# 5. Launch Streamlit dashboard
streamlit run streamlit/app.py

# 6. Optional REST API
uvicorn src.api.main:app --reload


🧭 Next Steps

 Finish Streamlit UI (confidence, evidence panels)

 Connect Power BI to Gold Layer

 Add Terraform deployment for Azure profile

 Integrate Prometheus + Grafana observability

 Publish public demo video and docs

👩‍💻 Author

Adriele Rocha Weisz
Data & AI Engineer | Zurich, Switzerland
🌐 LinkedIn
 • 📧 adriele.rocha.weisz@gmail.com












