from dataclasses import dataclass
from datetime import date, datetime

from Moexfilm.core.media.domain.models.utils import get_date


@dataclass
class SeasonTmdb:
    id: int
    air_date: date
    name: str
    overview: str
    poster_path: str
    season_number: int
    vote_average: float

    @staticmethod
    def from_dict(obj: any) -> 'SeasonTmdb':
        id = int(obj.get("id"))
        air_date = get_date(str(obj.get("air_date")))
        name = str(obj.get("name"))
        overview = str(obj.get("overview"))
        poster_path = str(obj.get("poster_path"))
        season_number = int(obj.get("season_number"))
        vote_average = float(obj.get("vote_average"))

        return SeasonTmdb(id, air_date, name, overview, poster_path, season_number, vote_average)
