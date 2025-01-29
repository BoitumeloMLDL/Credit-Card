# Fraud Detection Application

This is a **FastAPI-based** fraud detection application with a **minimal Vue frontend**. It runs a **custom ML model** to predict the likelihood of fraud from uploaded transaction CSV files. Results are displayed on the frontend and emailed to an administrator.

## 📌 Features
- **FastAPI Backend** – Handles file uploads, fraud prediction, and email notifications.
- **Vue Frontend (CDN)** – Provides a simple UI for uploading CSVs and viewing flagged transactions.
- **Custom ML Model** – Predicts fraud likelihood for each transaction.
- **Email Notifications** – Sends an email report of flagged transactions.
- **Dockerized Deployment** – Runs in containers, deployed using a script onto a **DigitalOcean Droplet**.
- **MailHog for Testing** – Captures emails locally for debugging.

---

## 🚀 Running the Demo

### **1️⃣ Prerequisites**
Ensure you have:
- **Docker & Docker Compose**
- **Python 3.11+ (for local development, if needed)**
- **A DigitalOcean Droplet (for deployment)**

---

### **2️⃣ Run Locally with Docker**
Clone the repository and start the application:

```bash
docker compose up --build -d
Access the Application:
    •    📊 Web UI: http://161.35.87.43:8000
    •    📩 Email Inbox (MailHog): http://161.35.87.43:8025

3️⃣ API Usage
The backend provides a single POST /upload endpoint for CSV file uploads.
Example Request
curl -X POST "http://localhost:8000/upload" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@transactions.csv"
Example JSON Response
[
  { "u_id": "12345", "prediction": 1 },
  { "u_id": "67890", "prediction": 1 },
  { "u_id": "54321", "prediction": 1 }
]
The response is also displayed on the frontend and sent via email.

🛠️ Deployment to DigitalOcean
The application is deployed using a custom deployment script.
Steps to Deploy:
    1    Ensure your DigitalOcean Droplet is running.
    2    Update the deploy.sh script with: SERVER_USER="your-username"
    3    SERVER_IP="your-server-ip"
    4    DEPLOY_PATH="/path/to/app"
    5    
    6    Run the deployment: ./deploy.sh
    7    
    8    Access your live application:
    ◦    Web UI: http://your-server-ip:8000
    ◦    Emails (MailHog): http://your-server-ip:8025

📂 Project Structure
.
├── backend/                # FastAPI application
│   ├── main.py             # API and logic
│   ├── ml_model.py         # Fraud prediction logic
│   ├── email_template.html # Email notification template
│   ├── requirements.txt    # Dependencies
│   └── Dockerfile          # Backend container setup
├── frontend/               # Vue frontend (served via FastAPI)
│   ├── index.html          # Main UI
│   ├── static/             # CSS, JS (if needed)
├── deploy.sh               # Deployment script
├── compose.yaml            # Docker setup
└── README.md               # This document

⚡ Technology Stack
    •    Backend: FastAPI (Python)
    •    Frontend: Vue (via CDN)
    •    ML Model: Hand-rolled fraud detection logic
    •    Emailing: MailHog (for local testing)
    •    Deployment: Docker + DigitalOcean Droplet

🚀 Enjoy Fraud Detection Simplified!
