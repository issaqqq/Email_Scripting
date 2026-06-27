import csv
import smtplib
import ssl
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Replace these with your dummy email and the App Password you generated
SENDER_EMAIL = "your_dummy_email@gmail.com"
APP_PASSWORD = "your_16_digit_app_password_here"

# --- Email Template ---
# Use {name} and {company} where you want the script to insert the data
SUBJECT = "Software Engineering Internship Application - John"
BODY_TEMPLATE = """\
Dear {name},

I hope this email finds you well. 

I am writing to express my strong interest in a Software Engineering Internship at {company}. I am currently studying Computer Science and have been following {company}'s recent work in the tech space, which aligns perfectly with my skills in Python and data analysis.

I have attached my resume for your review. Thank you for your time and consideration.

Best regards,
John Doe
"""

def send_cold_emails():
    # 1. Create a secure SSL context for the email server
    context = ssl.create_default_context()

    print("Connecting to email server...")
    
    # 2. Connect to Gmail's SMTP server
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(SENDER_EMAIL, APP_PASSWORD)
            print("Login successful!\n")

            # 3. Read the CSV file
            with open("internships.csv", mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                
                # 4. Loop through each row in the spreadsheet
                for row in reader:
                    company = row["Company"]
                    hr_name = row["HR_Name"]
                    target_email = row["Email"]

                    # Format the email body with the current row's data
                    custom_body = BODY_TEMPLATE.format(name=hr_name, company=company)

                    # Create the email message object
                    msg = MIMEMultipart()
                    msg["From"] = SENDER_EMAIL
                    msg["To"] = target_email
                    msg["Subject"] = SUBJECT
                    msg.attach(MIMEText(custom_body, "plain"))

                    # Send the email
                    print(f"Sending email to {hr_name} at {company} ({target_email})...")
                    server.sendmail(SENDER_EMAIL, target_email, msg.as_string())
                    
                    # 5. Pause for a few seconds to avoid triggering spam filters
                    time.sleep(2) 

        print("\nAll emails sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    send_cold_emails()