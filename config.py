import os

API_ID = os.environ.get("API_ID", "21008992")

API_HASH = os.environ.get("API_HASH", "da87f6dea5ed8cfe1a53617e33a35742")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7838532960:AAG0wI7_UxZROog6jA7sLJizr52KbhctMac")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", "7548265642" ))

LOG = "2441473161",

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7548265642").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


