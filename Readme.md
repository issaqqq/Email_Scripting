# 🚀 Cold Email Automation for Internships

## 📖 About
A Python script that automates internship applications by reading contacts from a CSV, personalizing email templates, and securely sending them via Gmail. It uses standard Python libraries and built-in delays to prevent spam-flagging.

## ✨ Features
* **Mass Automation:** Sends emails sequentially from a targeted spreadsheet list.
* **Dynamic Personalization:** Injects the recruiter's name and company name into the email body and subject.
* **Spam Prevention:** Includes a built-in time delay between emails to protect your sender reputation.
* **No External Dependencies:** Built entirely using Python's standard libraries (`smtplib`, `csv`, `email`).

## 🛠️ Prerequisites
* **Python 3.x** installed.
* A **Gmail Account** (A dedicated "dummy" account is recommended).
* **2-Step Verification** enabled on the Gmail account.
* A **16-Digit Google App Password** (Standard email passwords will be blocked).

## 🚀 Setup & Usage

### 1. Prepare your Data File
Create a file named `internships.csv` in the same directory as the script. Format it with these exact headers:
```csv
Company,HR_Name,Email
TechCorp,Sarah Smith,sarah.test@example.com