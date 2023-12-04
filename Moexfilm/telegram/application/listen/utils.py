from pyrogram.types import Message
from Moexfilm.core import MediaType
from Moexfilm.telegram.domain.message_tvshow_header import EPISODE_REGEX
import re


def get_type(message: Message) -> MediaType:
    text = message.text
    if bool(re.search(EPISODE_REGEX, text)):
        return MediaType.TV_SHOW
    return MediaType.MOVIE
