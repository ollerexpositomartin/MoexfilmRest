from datetime import date

from Moexfilm.core.media.domain.models.provider import Provider
from Moexfilm.core.media.domain.models.playable_media import PlayableMedia
from Moexfilm.core.media.domain.models.episode_tmdb import EpisodeTmdb
from dataclasses import dataclass


@dataclass
class Episode(PlayableMedia):
    air_date: date = None
    episode_number: int = None
    name: str = None
    overview: str = None
    still_path: str = None
    vote_average: float = None
    season_id: int = None

    @staticmethod
    def from_episode_tmdb(episode_tmdb: EpisodeTmdb):
        return Episode(
            tmdb_id=episode_tmdb.id,
            air_date=episode_tmdb.air_date,
            episode_number=episode_tmdb.episode_number,
            name=episode_tmdb.name,
            overview=episode_tmdb.overview,
            still_path=episode_tmdb.still_path,
            vote_average=episode_tmdb.vote_average
        )
