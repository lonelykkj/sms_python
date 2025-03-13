#2LZ9BMEXFNU7G73U6NGH78NZ RECOVERY CODE

from fastapi import FastAPI, HTTPException
from twilio.rest import Client

app = FastAPI()

ACCOUNT_SID = 'AC6e1ad92c274dd4b4e3475b5480a1ba88'
AUTH_TOKEN = '9c92e9d5352e4f2a46e2a0f06474a102'
PHONE_NUMBER = '+16505822353'

client = Client(ACCOUNT_SID, AUTH_TOKEN)

@app.post("/send-sms/")
async def send_sms(to: str, body: str):
    try:
        message = client.messages.create(
            from_=PHONE_NUMBER,
            to='+5512982998077',
            body='teste234'
        )
        return {'status': 'success', 'message_sid': message.sid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



