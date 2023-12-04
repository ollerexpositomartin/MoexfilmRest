from pyrogram.types import Message
from pyrogram import Client, filters
from queue import Queue
from Moexfilm.core import MediaType
from Moexfilm.telegram import MessageHeader, MessageMovieHeader, MessageTvShowHeader
from Moexfilm.telegram.application.listen.utils import get_type

headers: Queue = Queue()


@Client.on_message()
async def route_handler(_, m: Message):
    if await filters.text_filter(_, None, m):
        await message_header_handler(_, m)
        return
    if await filters.video_filter(_, None, m) or await filters.document_filter(_, None, m):
        await media_handler(_, m)


async def message_header_handler(_, m: Message):
    media_type: MediaType = get_type(m)
    header = None
    if media_type == MediaType.MOVIE:
        header = MessageMovieHeader(m.text)
    else:
        if media_type == MediaType.TV_SHOW:
            header = MessageTvShowHeader(m.text)

    if header:
        headers.put(header)


async def media_handler(_, m: Message):
    message_header: MessageHeader = headers.get()

    if not message_header:
        await m.reply_text("Before is needed a header")

    if isinstance(message_header, MessageMovieHeader):
        # busca pelicula tatatatata
        pass
    else:
        if isinstance(message_header, MessageTvShowHeader):
            # busca serie tatatatatata
            pass
