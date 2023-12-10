from pyrogram.types import Message
from Moexfilm.core.media.domain.models import MediaType, MediaSearchParams
from Moexfilm.telegram.domain import MessageHeader, MessageTvShowHeader
from Moexfilm.telegram.domain.message_tvshow_header import SEASON_EPISODE_REGEX
import re


def get_type(message: Message) -> MediaType:
    text = message.text
    if bool(re.search(SEASON_EPISODE_REGEX, text)):
        return MediaType.TV_SHOW
    return MediaType.MOVIE


def get_search_params(message: MessageHeader) -> MediaSearchParams:
    if isinstance(message, MessageTvShowHeader):
        return MediaSearchParams(
            title=message.title,
            release_date=message.release_date,
            season=int(message.season),
            episode=int(message.episode),
            type=MediaType.TV_SHOW
        )

    return MediaSearchParams(
        title=message.title,
        release_date=message.release_date,
        season=None,
        episode=None,
        type=MediaType.MOVIE
    )
