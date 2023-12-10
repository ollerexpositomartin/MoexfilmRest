from Moexfilm.core.media.domain.models import MediaTmdb, MediaSearchParams, Movie, TvShow, Season, SeasonTmdb, \
    EpisodeTmdb, Episode
from Moexfilm.core.media.domain.repositories import TmdbRepository


class TmdbService:

    def __init__(self, tmdb_repository: TmdbRepository):
        self.tmdb_repository = tmdb_repository

    def search_movie(self, media_search_params: MediaSearchParams) -> Movie:
        movie_tmdb: MediaTmdb = self.tmdb_repository.search_media(media_search_params)
        return Movie.from_media_tmdb(movie_tmdb)

    def search_tv_show(self, media_search_params: MediaSearchParams) -> TvShow:
        tv_show_tmdb: MediaTmdb = self.tmdb_repository.search_media(media_search_params)
        return TvShow.from_media_tmdb(tv_show_tmdb)

    def search_season(self, tv_show_id: int, season_n) -> Season:
        season_tmdb: SeasonTmdb = self.tmdb_repository.search_season(tv_show_id, season_n)
        return Season.from_season_tmdb(season_tmdb)

    def search_episode(self, tv_show_id: int, season_n, episode_n) -> Episode:
        episode_tmdb: EpisodeTmdb = self.tmdb_repository.search_episode(tv_show_id, season_n,
                                                                        episode_n)
        return Episode.from_episode_tmdb(episode_tmdb)
