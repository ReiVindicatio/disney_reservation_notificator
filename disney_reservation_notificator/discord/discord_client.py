from dotenv import load_dotenv
import os
import requests
import json

load_dotenv('.app-env')

def send_message(message: str):
    data = { "content": message }
    try:
        response = requests.post(
            os.getenv('DISCORD_WEBHOOK_URL'),
            json.dumps(data).encode(),
            headers={"Content-Type": "application/json"}
        )
    except Exception as e:
        print(e)