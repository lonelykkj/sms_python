from fastapi import FastAPI, HTTPException
from twilio.rest import Client

app = FastAPI()

ACCOUNT_SID = 'twiolio account sid'
AUTH_TOKEN = 'twilio auth token'
PHONE_NUMBER = 'twilio number'

client = Client(ACCOUNT_SID, AUTH_TOKEN)

@app.post("/send-sms/")
async def send_sms(to: str, body: str):
    try:
        message = client.messages.create(
            from_=PHONE_NUMBER,
            to='your number',
            body='Hello World!'
        )
        return {'status': 'success', 'message_sid': message.sid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



