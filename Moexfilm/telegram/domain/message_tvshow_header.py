from pyrogram.types import Message
import re
from Moexfilm.telegram.domain.message_header import MessageHeader

EPISODE_REGEX = "^[A-Za-z ]+(s| )\\d+(e|x)\\d+$"
class MessageTvShowHeader(MessageHeader):
    season: int
    episode: int

    def __init__(self,message: Message):
        self.title = self._get_title(message.text)

    def _get_title(self,text:str) -> str :
        if bool(re.search(EPISODE_REGEX, text)):
            print("")
        return ""