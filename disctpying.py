import requests
import time
from dotenv import dotenv_values

# Load variables from .env file
config = dotenv_values('.env')

# Access the variables using the loaded config
channel_id = config['CHANNEL_ID']
token = config['TOKEN']

url = f"https://discord.com/api/v9/channels/{channel_id}/typing"
headers = {
    "Authorization": token
}

while True:
    response = requests.post(url, headers=headers)
    
    if response.status_code == 204:
        print("POST request sent successfully.")
    else:
        print(f"POST request failed with status code: {response.status_code}")
    
    time.sleep(7)
