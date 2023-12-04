import os
from pyrogram import Client
from Moexfilm.context import application_context

config = application_context.config
sessions_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sessions")

Bot = Client(
    name=config.NAME,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    workdir=sessions_dir,
    plugins={"root": "Moexfilm/telegram/application/listen"},
    sleep_threshold=60,
    workers=6,
    bot_token=config.BOT_TOKEN,
    in_memory=True
)
