from datetime import date

from Moexfilm.core.media.domain.models.media_type import MediaType
from dataclasses import dataclass
from typing import List


@dataclass
class Media:
    tmdb_id: int = None
    title: str = None
    overview: str = None
    backdrop_path: str = None
    popularity: float = None
    poster_path: str = None
    release_date: date = None
    vote_average: float = None
    genre_ids: List[int] = None
    type: MediaType = None

