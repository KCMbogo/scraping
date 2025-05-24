import subprocess, json
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from twilio.twiml.messaging_response import MessagingResponse
from send_message import send_message


app = FastAPI()

@app.post("/whatsapp")
async def whatsapp(request: Request):
    form = await request.form()
    body = form.get('Body', '')
    print(f"Got message: {body}")

    response = MessagingResponse()

    title, location = [x.strip() for x in body.split(', ')]
    try:
        subprocess.run(['python', 'job_scrapping/job_scraping.py', title, location], check=True)
    except Exception as e:
        print(f"An error occured: {e}")

    with open("scraped/jobs.json", "r", encoding="utf-8") as f:
        jobs = json.load(f)
    # message = f"Top Job: {jobs[0]['title']} at {jobs[0]['company']} in {jobs[0]['location']}\n{jobs[0]['link']}"

    for job in jobs:
        message = (
            f"TITLE: *{job['title']}*\n"
            f"COMPANY: *{job['company']}*\n"
            f"LOCATION: _{job['location']}_\n"
            f"*For More Info:*\n"
            f"{job['link']}"
        )
        send_message(message, image_url=job['image'])
        response.message(message)
    return PlainTextResponse(str(response), media_type="application/xml")