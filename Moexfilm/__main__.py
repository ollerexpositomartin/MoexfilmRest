import asyncio
import logging
import sys
from fastapi import FastAPI
from Moexfilm.telegram import Bot
from Moexfilm.context import application_context
import uvicorn
from Moexfilm.telegram.interfaces.download import download_router

app = FastAPI()
app.include_router(download_router)
config = application_context.config

loop = asyncio.get_event_loop()
logging.basicConfig(
    level=logging.DEBUG if config.DEBUG else logging.INFO,
    datefmt="%d/%m/%Y %H:%M:%S",
    format="[%(asctime)s][%(name)s][%(levelname)s] ==> %(message)s",
    handlers=[logging.StreamHandler(stream=sys.stdout),
              logging.FileHandler("streambot.log", mode="a", encoding="utf-8")], )
logging.getLogger("uvicorn").setLevel(logging.DEBUG if config.DEBUG else logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.INFO if config.DEBUG else logging.ERROR)
logging.getLogger("uvicorn.server").setLevel(logging.DEBUG if config.DEBUG else logging.ERROR)


async def start_services():
    print("""
  __  __                  __ _ _           
 |  \/  | ___   _____  __/ _(_) |_ __ ___  
 | |\/| |/ _ \ / _ \ \/ / |_| | | '_ ` _ \ 
 | |  | | (_) |  __/>  <|  _| | | | | | | |
 |_|  |_|\___/ \___/_/\_\_| |_|_|_| |_| |_|
    """)
    await Bot.start()
    uvi_config = uvicorn.Config(app, port=8080, host='0.0.0.0')
    server = uvicorn.Server(uvi_config)
    await server.serve()


if __name__ == "__main__":
    loop.run_until_complete(start_services())
