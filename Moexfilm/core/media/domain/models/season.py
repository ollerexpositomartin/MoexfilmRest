from datetime import date
from typing import List

from Moexfilm.core.media.domain.models.season_tmdb import SeasonTmdb
from Moexfilm.core.media.domain.models.episode import Episode
from dataclasses import dataclass, field


@dataclass
class Season:
    tmdb_id: int = None
    tv_show_id: int = None
    air_date: date = None
    poster_path: str = None
    season_number: int = None
    vote_average: float = None
    episodes: List[Episode] = field(default_factory=list)

    @staticmethod
    def from_season_tmdb(season_tmb: SeasonTmdb):
        return Season(
            tmdb_id=season_tmb.id,
            tv_show_id=0,
            air_date=season_tmb.air_date,
            poster_path=season_tmb.poster_path,
            season_number=season_tmb.season_number,
            vote_average=season_tmb.vote_average,
            episodes=[]
        )
