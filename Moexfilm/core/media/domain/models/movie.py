from dataclasses import dataclass
from Moexfilm.core.media.domain.models.playable_media import PlayableMedia
from Moexfilm.core.media.domain.models.media_tmdb import MediaTmdb
from Moexfilm.core.media.domain.models.media_type import MediaType
from Moexfilm.core.media.domain.models.media import Media


@dataclass
class Movie(Media, PlayableMedia):

    @staticmethod
    def from_media_tmdb(movie_tmdb: MediaTmdb) -> 'Movie':
        return Movie(
            type=MediaType.MOVIE,
            tmdb_id=movie_tmdb.id,
            title=movie_tmdb.title,
            overview=movie_tmdb.overview,
            backdrop_path=movie_tmdb.backdrop_path,
            genre_ids=movie_tmdb.genre_ids,
            popularity=movie_tmdb.popularity,
            poster_path=movie_tmdb.poster_path,
            release_date=movie_tmdb.release_date,
            vote_average=movie_tmdb.vote_average
        )
