from datetime import date
from typing import Any
from dataclasses import dataclass

from Moexfilm.core.media.domain.models.utils import get_date


@dataclass
class EpisodeTmdb:
    air_date: date
    episode_number: int
    name: str
    overview: str
    id: int
    season_number: int
    still_path: str
    vote_average: float

    @staticmethod
    def from_dict(obj: Any) -> 'EpisodeTmdb':
        _air_date = get_date(str(obj.get("air_date")))
        _episode_number = int(obj.get("episode_number"))
        _name = str(obj.get("name"))
        _overview = str(obj.get("overview"))
        _id = int(obj.get("id"))
        _season_number = int(obj.get("season_number"))
        _still_path = str(obj.get("still_path"))
        _vote_average = float(obj.get("vote_average"))

        return EpisodeTmdb(_air_date, _episode_number, _name, _overview, _id, _season_number, _still_path,
                           _vote_average)
