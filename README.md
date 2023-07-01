# Discord Typing Indicator

This Python script sends a POST request to a Discord channel, simulating the typing indicator. It can be used to create the illusion of a user typing in a specific channel.

## Usage

1. Clone the repository or download the script file.

2. Install the required dependencies:
   ```bash
   pip install requests python-dotenv
Create a .env file in the same directory as the script and add the following variables:



CHANNEL_ID=<Your Discord Channel ID>
TOKEN=<Your Discord Authorization Token>

Get your Discord Authorization Token:

Open Discord in a web browser.
Right-click and select "Inspect" or "Inspect Element".
In the browser developer tools, go to the "Network" tab.
Send a message in the desired channel.
Look for a request with the URL format /api/v9/channels/<Channel ID>/typing.
In the request headers, find the "Authorization" header. Copy the token value.
Get your Discord Channel ID:

Open Discord in a web browser.
Right-click on the desired channel and select "Copy ID".
Paste the copied ID into the CHANNEL_ID variable in the .env file.
Run the script:

python script.py
The script will send a POST request to the specified Discord channel every 7 seconds, simulating a typing indicator.

Note: Keep the .env file secure and do not share it, as it contains sensitive information.

