import os
from io import StringIO
from email.message import EmailMessage

import joblib
import pandas as pd
import aiosmtplib
from fastapi import BackgroundTasks, FastAPI, UploadFile
from fastapi.responses import FileResponse, HTMLResponse
from jinja2 import Environment, FileSystemLoader
from pydantic import BaseModel

app = FastAPI()
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

# Load the separately saved scaler and model
scaler = joblib.load("model/scaler.pkl")
model = joblib.load("model/model.pkl")

# Define the indices of the features that need scaling
scaled_feature_indices = ["Time", "Amount"]  # Replace with actual indices
new_feature_names = ["Time_scaled", "Amount_scaled"]


def predict(dataset: pd.DataFrame):
    # Select only the features that need scaling and apply transformation

    dataset["Time_scaled"] = scaler.transform(dataset["Time"].values.reshape(-1, 1))
    dataset["Amount_scaled"] = scaler.transform(dataset["Amount"].values.reshape(-1, 1))

    # Drop Time and Amount
    features_df = dataset.drop(columns=["Time", "Amount", "u_id","Class"], axis=1)

    # Make prediction
    predictions = model.predict(features_df)

    return predictions


async def send_email(flagged_transactions: list[dict]):
    """Send email notification after prediction"""

    if not flagged_transactions:
        return

    template = env.get_template("email.html")
    email_content = template.render(transactions=flagged_transactions)

    msg = EmailMessage()
    msg["From"] = "alerts@example.com"
    msg["To"] = "agent@example.com"
    msg["Subject"] = "Fraud Alert: Flagged Transactions"
    msg.set_content("Your email client does not support HTML.")
    msg.add_alternative(email_content, subtype="html")

    await aiosmtplib.send(msg, hostname="mailhog", port=1025)


@app.get("/", response_class=HTMLResponse)
async def upload_page():
    return FileResponse(os.path.join(TEMPLATES_DIR, "index.html"))


@app.post("/upload/")
async def upload_csv(file: UploadFile, background_tasks: BackgroundTasks):
    """Consume the uploaded files for prediction"""

    content = await file.read()
    df = pd.read_csv(StringIO(content.decode("utf-8")), index_col=0)

    predictions = predict(df)

    predictions_df = pd.DataFrame(df["u_id"])
    predictions_df["maybe_fraud"] = predictions

    flagged_transactions = predictions_df[predictions_df["maybe_fraud"] == 1]
    output = flagged_transactions.to_dict(orient='records')

    background_tasks.add_task(send_email, output)

    return output
