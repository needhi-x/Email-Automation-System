import pandas as pd
import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage
from datetime import datetime
import logging

# =========================
# ENV SETUP
# =========================
load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# =========================
# LOGGING SETUP
# =========================
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =========================
# LOAD DATA
# =========================
def load_data():
    contacts = pd.read_csv("data/contacts.csv")
    reminders = pd.read_csv("data/reminders.csv")
    return contacts, reminders

# =========================
# LOAD TEMPLATE
# =========================
def load_template():
    with open("email_template.txt", "r") as f:
        return f.read()

# =========================
# SEND EMAIL FUNCTION
# =========================
def send_email(to_email, subject, body):
    try:
        msg = EmailMessage()
        msg["From"] = EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.set_content(body)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
        server.quit()

        logging.info(f"Email sent to {to_email}")
        return "SUCCESS"

    except Exception as e:
        logging.error(f"Failed for {to_email}: {e}")
        return "FAILED"

# =========================
# PROCESS EMAILS
# =========================
def process_emails():
    contacts, reminders = load_data()
    template = load_template()

    report = []

    for _, row in reminders.iterrows():
        email = row["email"]
        message = row["message"]
        date = row["date"]

        contact = contacts[contacts["email"] == email]

        name = contact.iloc[0]["name"] if not contact.empty else "User"

        final_msg = template.format(
            name=name,
            message=message,
            date=date
        )

        status = send_email(email, "Reminder Notification", final_msg)

        report.append({
            "email": email,
            "status": status,
            "time": datetime.now()
        })

    df = pd.DataFrame(report)
    os.makedirs("outputs", exist_ok=True)
    df.to_csv("outputs/report.csv", index=False)

    print("✅ Automation Completed")