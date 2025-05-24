# 💼 LinkedIn Job Scraper & WhatsApp Bot

This is a Python-based automation tool that lets you **scrape jobs from LinkedIn** based on a keyword and location, and then **sends the job listings to your WhatsApp** using Twilio's WhatsApp API.

> Perfect for job seekers, recruiters, or anyone looking to get job alerts right in their WhatsApp chat.

---

## ✨ Features

- 🔍 Scrapes real-time job listings from LinkedIn using Playwright.
- 📩 Sends the top results directly to WhatsApp.
- 🧠 Well-formatted WhatsApp messages with job details.
- 🖼 Optional company logos using Clearbit.
- 🌐 Runs as a FastAPI server (can be integrated with ngrok or hosted on a VPS).

---

## 📦 Project Structure

linkedin_jobs_bot/
├── main.py # FastAPI server
├── scraper.py # LinkedIn job scraper (Playwright)
├── twilio_utils.py # WhatsApp message sender using Twilio
├── scraped/jobs.json # Scraped job results
├── requirements.txt
└── README.md


---

## 🚀 How It Works

1. Send a WhatsApp message with a keyword and location (e.g. `Python, America`) to your Twilio Sandbox number.
2. The FastAPI server receives the message.
3. The scraper fetches job listings from LinkedIn.
4. The best jobs are sent back to your WhatsApp in a clean, structured format with optional images.

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/KCMbogo/scrapping.git
cd scrapping

### 2. Create virtual environment and install dependencies
pip install -r requirements.txt
playwright install

### 3. Setup .env
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token


