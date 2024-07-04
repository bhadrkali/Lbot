# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25018366"))
API_HASH = getenv("API_HASH", "03194f91ff9af028447f66c0d62e7e77")
BOT_TOKEN = getenv("BOT_TOKEN", "7267867962:AAE_GZLYhWj0bXnyvHrp9ziSxdw2TwdGIyE")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7333826463").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Cluster0:cluster0@veerbhadra.qrqeg0n.mongodb.net/?retryWrites=true&w=majority&appName=veerbhadra")
LOG_GROUP = getenv("LOG_GROUP", "-1002216387353")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002216700896"))
