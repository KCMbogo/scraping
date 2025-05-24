# 💼 Job Scraper & WhatsApp Bot

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
```
scrapping/
├── job_scrapping/
│   ├── app.py               # FastAPI endpoint to call the job_scraping.py module
│   ├── job_scraping.py      # Playwright scraping logic
├── scraped/jobs.json        # Scraped job results
├── requirements.txt
└── README.md
```


---

## 🚀 How It Works

1. Send a WhatsApp message with a keyword and location (e.g. `Python Developer, Tanzania`) to your Twilio Sandbox number.
2. The FastAPI server receives the message.
3. The scraper fetches job listings from LinkedIn.
4. The best jobs are sent back to your WhatsApp in a clean, structured format with images.

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/KCMbogo/scraping.git
cd scrapping
```

### 2. Create virtual environment and install dependencies
```bash
python -m venv .venv
source .venv/bin/activate # for linux or
.\.venv\Scripts\activate # for windows
pip install -r requirements.txt
playwright install # to install the browser engines needed by playwright
```

### 3. Setup .env
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
> NOTE: You need to create a twilio account to get these credentials: [Twilio](https://www.twilio.com/)

### 4. Run the server
```bash
uvicorn job_scrapping.job_scrapping:app --host 127.0.0.1 --port 8000
```

### 5. Make available to Internet using Ngrok
> Make sure you install ngrok based on you operating system: [Ngrok](https://ngrok.com/downloads/)
```bash
ngrok http 8000 # For linux

# For windows go search how.
```
---

## 💬 Format
### WhatsApp Message
> Python Developer, Tanzania

### Message Response
🖼 Company logo shown if available. <br>
*🔹 Python Developer* <br>
*🏢 Google* <br>
📍 _New York, NY_ <br>
🔗 https://linkedin.com/jobs/view/...

---

