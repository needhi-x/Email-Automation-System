from fastapi import FastAPI
from main import process_emails

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Email Automation API Running"}

@app.post("/run-emails")
def run_emails():
    process_emails()
    return {"status": "Emails processed successfully"}