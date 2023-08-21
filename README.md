Telegram Bulk Group Message Sender - Broadcaster

# TelegramGroupBroadcast
This is a python code which send messages to all your telegram groups with just 1 click


Automatically send a message to multiple Telegram groups and channels at once using the Telethon Python API.

Prerequisites
Python: This script is written in Python. Make sure you have Python installed on your machine.
Telethon: A Python Telegram client used to interact with the Telegram API. Install it using pip:
bash
Copy code
pip install telethon
Telegram API credentials: You'll need to get your api_id and api_hash from Telegram's developer portal. Replace the placeholders 'id' and 'hash' in the code with your actual credentials.
Usage
Clone/download the script to your local machine.
Run the script:
bash
Copy code
python main.py
You'll be prompted to input the message you want to broadcast. Type in your message and hit enter.
The script will then attempt to send the message to all the groups and channels in which you are a member or have the rights to send messages.
It will display the status (success/failure) for each group or channel.
Notes
The script currently fetches a maximum of 200 dialogues due to the limit=200 parameter. You can adjust this number if necessary.
Ensure you have the necessary rights to send messages in groups and channels. Otherwise, the script will display an error for that particular group or channel.
Continuous use of this script in a short span of time may lead to rate limits or bans by Telegram due to spammy behavior. Use responsibly.
License
This project is open-source and free to use. However, please ensure you're adhering to Telegram's terms of service and guidelines when using and distributing this tool.
