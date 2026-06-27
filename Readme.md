# 🚀 Cold Email Automation for Internships

## 📖 About
A Python automation tool that streamlines internship applications by sending personalized, delay-paced cold emails directly from a CSV list. 

This script reads recruiter contact details from a spreadsheet, dynamically injects the data into a personalized email template, and securely dispatches the emails using Gmail's SMTP server. It uses built-in Python libraries (`smtplib`, `csv`) and features automated delays to respect server limits and prevent spam-flagging.

## ✨ Features
* **Mass Automation:** Sends emails sequentially from a targeted spreadsheet list.
* **Dynamic Personalization:** Injects the recruiter's name and company name into the email body and subject.
* **Spam Prevention:** Includes a built-in time delay between emails to protect your sender reputation.
* **No External Dependencies:** Built entirely using Python's standard libraries.

## 🛠️ Prerequisites
* **Python 3.x** installed on your machine.
* A **Gmail Account** (A dedicated "dummy" account is highly recommended).
* **2-Step Verification** enabled on the Gmail account.
* A **16-Digit Google App Password** (Standard email passwords will be blocked by Google).

---

## 📂 Project Setup & Files

Create a new folder on your computer for this project. Inside that folder, you will create two files: `internships.csv` and `main.py`.

### Step 1: The Data File (`internships.csv`)
Create a file named `internships.csv` in your project folder. Format it with these exact headers and populate it with your target list:

```csv
Company,HR_Name,Email
TechCorp,Sarah Smith,sarah.test@example.com
DataSoft Systems,Mr. Johnson,test_email_2@example.com
CloudNet LLC,Hiring Team,test_email_3@example.com