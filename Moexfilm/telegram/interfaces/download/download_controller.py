import logging
import math
import mimetypes
from fastapi import APIRouter, Request
from fastapi.openapi.models import Response
from fastapi.responses import StreamingResponse
from Moexfilm.telegram import Bot
from Moexfilm.telegram.interfaces.download import utils

download_router = APIRouter()


@download_router.get("/download/telegram/{file_id}")
async def download_file(request: Request, file_id: int):
    try:
        return await media_streamer_out_hash(request, int(file_id))

    except Exception as e:
        logging.critical(str(e), exc_info=True)


class_cache = {}


async def media_streamer_out_hash(request: Request, message_id: int):
    range_header = request.headers.get("Range", 0)
    tg_connect = utils.ByteStreamer(Bot)
    logging.debug("before calling get_file_properties")
    file_id = await tg_connect.get_file_properties(message_id)
    logging.debug("after calling get_file_properties")

    index = 0

    file_size = file_id.file_size

    if range_header:
        from_bytes, until_bytes = range_header.replace("bytes=", "").split("-")
        from_bytes = int(from_bytes)
        until_bytes = int(until_bytes) if until_bytes else file_size - 1
    else:
        from_bytes = request.headers.get("range-start") or 0
        until_bytes = (request.headers.get("range-end") or file_size) - 1

    if (until_bytes > file_size) or (from_bytes < 0) or (until_bytes < from_bytes):
        return Response(
            status=416,
            body="416: Range not satisfiable",
            headers={"Content-Range": f"bytes */{file_size}"},
        )

    chunk_size = 1024 * 1024
    until_bytes = min(until_bytes, file_size - 1)

    offset = from_bytes - (from_bytes % chunk_size)
    first_part_cut = from_bytes - offset
    last_part_cut = until_bytes % chunk_size + 1

    req_length = until_bytes - from_bytes + 1
    part_count = math.ceil(until_bytes / chunk_size) - math.floor(offset / chunk_size)
    body = tg_connect.yield_file(
        file_id, index, offset, first_part_cut, last_part_cut, part_count, chunk_size
    )
    mime_type = file_id.mime_type
    file_name = utils.get_name(file_id)
    disposition = "attachment"

    if not mime_type:
        mime_type = mimetypes.guess_type(file_name)[0] or "application/octet-stream"

    if "video/" in mime_type or "audio/" in mime_type or "/html" in mime_type:
        disposition = "inline"

    headers = {
        "Content-Type": f"{mime_type}",
        "Content-Range": f"bytes {from_bytes}-{until_bytes}/{file_size}",
        "Content-Length": str(req_length),
        "Content-Disposition": f'{disposition}; filename="{file_name}"',
        "Accept-Ranges": "bytes",
    }

    return StreamingResponse(
        status_code=206 if range_header else 200,
        content=body,
        headers=headers,
    )
