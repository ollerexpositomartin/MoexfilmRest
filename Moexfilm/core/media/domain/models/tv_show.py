from Moexfilm.core.media.domain.models.media_type import MediaType
from Moexfilm.core.media.domain.models.provider import Provider
from Moexfilm.core.media.domain.models.media_tmdb import MediaTmdb
from Moexfilm.core.media.domain.models.media import Media
from Moexfilm.core.media.domain.models.season import Season
from typing import List
from dataclasses import dataclass, field


@dataclass
class TvShow(Media):
    seasons: List[Season] = field(default_factory=list)

    @staticmethod
    def from_media_tmdb(tv_show_tmdb: MediaTmdb) -> 'TvShow':
        return TvShow(
            type=MediaType.TV_SHOW,
            tmdb_id=tv_show_tmdb.id,
            title=tv_show_tmdb.title,
            overview=tv_show_tmdb.overview,
            backdrop_path=tv_show_tmdb.backdrop_path,
            genre_ids=tv_show_tmdb.genre_ids,
            popularity=tv_show_tmdb.popularity,
            poster_path=tv_show_tmdb.poster_path,
            release_date=tv_show_tmdb.release_date,
            vote_average=tv_show_tmdb.vote_average)
