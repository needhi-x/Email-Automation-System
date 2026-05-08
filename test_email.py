import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage

# Load .env file
load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Create email object
msg = EmailMessage()
msg["Subject"] = "Test Email"
msg["From"] = EMAIL
msg["To"] = EMAIL

# Email body (now emoji will work)
msg.set_content("Hello Nidhi! Your email automation system is working 🎉")

# Setup server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# Login
server.login(EMAIL, PASSWORD)

# Send email
server.send_message(msg)

print("✅ Email sent successfully!")

# Close server
server.quit()