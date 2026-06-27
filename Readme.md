# 📧 Internship Application Automation

A Python-based automation tool that streamlines internship applications by reading recruiter details from a CSV file, personalizing email templates, and securely sending emails through Gmail's SMTP server.

## 🚀 Features

- Read recruiter and company information from a CSV file
- Automatically personalize email content using placeholders
- Secure email transmission using Gmail SMTP over SSL
- Built-in delay between emails to reduce the risk of spam detection
- Simple and lightweight implementation using Python's standard libraries
- Easy to customize email subject and body

---

## 🛠️ Technologies Used

- Python 3
- `csv`
- `smtplib`
- `ssl`
- `time`
- `email.mime`

---

## 📂 Project Structure

```
.
├── main.py             # Main automation script
├── internship.csv      # CSV containing recruiter information
└── README.md
```

---

## 📋 CSV Format

Create a CSV file with the following columns:

| Company | HR_Name | Email |
|----------|---------|-------|
| Google | John Smith | john@google.com |
| Microsoft | Jane Doe | jane@microsoft.com |

Example:

```csv
Company,HR_Name,Email
Google,John Smith,john@google.com
Microsoft,Jane Doe,jane@microsoft.com
```

---

## ⚙️ Configuration

Before running the script, update the following variables in `main.py`:

```python
SENDER_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_16_digit_app_password"
```

Also customize:

- Email subject
- Email body template
- Your name and signature

---

## 📩 Email Personalization

The email template supports dynamic placeholders:

- `{name}` → Recruiter's name
- `{company}` → Company name

Example:

```python
BODY_TEMPLATE = """
Dear {name},

I am writing to express my interest in a Software Engineering Internship at {company}.

Best Regards,
John Doe
"""
```

Each recipient receives a personalized email.

---

## ▶️ How to Run

1. Clone the repository.

```bash
git clone https://github.com/yourusername/internship-email-automation.git
```

2. Navigate to the project directory.

```bash
cd internship-email-automation
```

3. Update your Gmail credentials and email template.

4. Prepare the CSV file.

5. Run the script.

```bash
python main.py
```

---

## 🔒 Gmail Setup

To use Gmail SMTP:

1. Enable **2-Step Verification** on your Google account.
2. Generate an **App Password**.
3. Replace the placeholder App Password in the script.

> **Never share your App Password or commit it to GitHub.**

---

## ⏱️ Spam Prevention

The script automatically waits **2 seconds** between sending emails using:

```python
time.sleep(2)
```

This helps reduce the likelihood of triggering spam filters.

---

## 📌 Future Improvements

- Resume attachment support
- HTML email templates
- Logging successful and failed emails
- Email tracking
- GUI interface using Tkinter
- Support for multiple email providers
- Configuration through environment variables

---

## ⚠️ Disclaimer

This project is intended for educational and personal use. Always obtain permission before sending bulk emails and comply with Gmail's sending policies and applicable anti-spam regulations.

---
