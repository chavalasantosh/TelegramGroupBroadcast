from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import Channel, Chat

api_id = 'api_id'
api_hash = 'api_hash'
message = str(input("Your message goes here:- "))

with TelegramClient('anon', api_id, api_hash) as client:
    if not client.is_user_authorized():
        client.start()

    all_dialogs = client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=client.get_input_entity('me'),
        limit=200,
        hash=0
    ))

    all_groups = [chat for chat in all_dialogs.chats if isinstance(chat, (Channel, Chat))]

    for group in all_groups:
        try:
            client.send_message(group.id, message)
            print(f"Message sent to {group.title}")
        except Exception as e:
            print(f"Could not send message to {group.title}. Error: {e}")

print("Finished sending messages.")


#if you need multithread implementation for this code let me know
