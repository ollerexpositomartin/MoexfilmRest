from datetime import date
from typing import List
from typing import Any
from dataclasses import dataclass

from Moexfilm.core.media.domain.models.utils import get_date


@dataclass
class MediaTmdb:
    adult: bool
    backdrop_path: str
    genre_ids: List[int]
    id: int
    original_language: str
    original_title: str
    overview: str
    popularity: float
    poster_path: str
    release_date: date
    title: str
    video: bool
    vote_average: float
    vote_count: int

    @staticmethod
    def from_dict(obj: Any) -> 'MediaTmdb':
        _adult = bool(obj.get("adult"))
        _backdrop_path = str(obj.get("backdrop_path"))
        _genre_ids = obj.get("genre_ids")
        _id = int(obj.get("id"))
        _original_language = str(obj.get("original_language"))
        _original_title = str(obj.get("original_title"))
        _overview = str(obj.get("overview"))
        _popularity = float(obj.get("popularity"))
        _poster_path = str(obj.get("poster_path"))
        _release_date = get_date(str(obj.get("release_date"))
                                 if obj.get("release_date") else str(obj.get("first_air_date")))
        _title = str(obj.get("title")) if obj.get("title") else str(obj.get("name"))
        _video = bool(obj.get("video"))
        _vote_average = float(obj.get("vote_average"))
        _vote_count = int(obj.get("vote_count"))
        return MediaTmdb(_adult, _backdrop_path, _genre_ids, _id, _original_language, _original_title, _overview,
                         _popularity, _poster_path, _release_date, _title, _video, _vote_average, _vote_count)
