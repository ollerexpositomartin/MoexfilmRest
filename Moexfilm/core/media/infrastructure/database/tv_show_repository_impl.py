from typing import List, Dict
from Moexfilm.core.media.domain.models import Episode, Season, TvShow, Provider, MediaType
from Moexfilm.core.media.domain.repositories import TvShowRepository
from Moexfilm.core.media.infrastructure.database import MediaRepositoryImpl
from Moexfilm.core.media.infrastructure.database.moexfilm_db_connector import MoexfilmDbConnector


class TvShowRepositoryImpl(TvShowRepository, MediaRepositoryImpl):

    def save_tv_show(self, tv_show: TvShow):
        with MoexfilmDbConnector() as conn:
            self._save_media(tv_show, conn)
            if tv_show.seasons:
                for season in tv_show.seasons:
                    self.save_season(season, conn)

    def get_all_tv_shows(self) -> List[TvShow]:
        with MoexfilmDbConnector() as conn:
            results = conn.execute("""
            SELECT * FROM tv_show;
            """)
            return self._populate_tv_shows(results)

    def _populate_tv_show(self, item: Dict):
        return TvShow(
            tmdb_id=item[0],
            title=item[1],
            overview=item[2],
            backdrop_path=item[3],
            popularity=item[4],
            poster_path=item[5],
            release_date=item[6],
            vote_average=item[7],
            type=MediaType.TV_SHOW
        )

    def _populate_tv_shows(self, result: List[Dict]):
        tv_shows = []
        for item in result:
            tv_shows.append(
                self._populate_tv_show(item)
            )
        return tv_shows

    def get_all_seasons(self, tv_show_id: int) -> List[Season]:
        with MoexfilmDbConnector() as conn:
            results = conn.execute("""
                 SELECT * FROM public.season WHERE tv_show_id = %s;
                """, (tv_show_id,))
            return self._populate_seasons(results)

    def _populate_season(self, item: Dict) -> Season:
        return Season(
            tmdb_id=item[0],
            tv_show_id=item[1],
            air_date=item[2],
            poster_path=item[3],
            season_number=item[4],
            vote_average=item[5]
        )

    def _populate_seasons(self, results: List[Dict]):
        seasons = []
        for item in results:
            seasons.append(
                self._populate_season(item)
            )
        return seasons

    def get_all_episodes(self, season_id: str) -> List[Episode]:
        with MoexfilmDbConnector() as conn:
            results = conn.execute("""
            SELECT e.tmdb_id,pmp.id,e.season_id,pmp.provider,e.episode_number,e.air_date,e.name,e.overview,e.still_path,e.vote_average
            FROM episode e
            INNER JOIN playable_media_provider pmp on e.tmdb_id = pmp.tmdb_id WHERE e.season_id = %s;
                """, (season_id,))
            return self._populate_episodes(results)

    def _populate_episode(self, item: Dict) -> Episode:
        return Episode(
            tmdb_id=item[0],
            season_id=item[1],
            provider=Provider[item[2]],
            air_date=item[3],
            name=item[4],
            overview=item[5],
            still_path=item[6],
            vote_average=item[7]
        )

    def _populate_episodes(self, results: List[Dict]):
        episodes = []
        for item in results:
            episodes.append(
                self._populate_episode(item)
            )
        return episodes

    def save_season(self, season: Season, conn=None):
        query = """INSERT INTO public.season (tmdb_id, tv_show_id, air_date, poster_path, season_number, vote_average)
        VALUES (%s, %s, %s, %s, %s, %s)"""

        params = (season.tmdb_id, season.tv_show_id, season.air_date, season.poster_path, season.season_number,
                  season.vote_average)

        if conn:
            conn.execute(query, params)
            if season.episodes:
                for episode in season.episodes:
                    self.save_episode(episode, conn)
            return

        with MoexfilmDbConnector() as conn:
            conn.execute(query, params)
            if season.episodes:
                for episode in season.episodes:
                    self.save_episode(episode, conn)

    def save_episode(self, episode: Episode, conn=None):
        query = """ INSERT INTO public.episode (tmdb_id, season_id, air_date,episode_number, name, overview, still_path, vote_average)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

        params = (episode.tmdb_id, episode.season_id, episode.air_date, episode.episode_number, episode.name,
                  episode.overview, episode.still_path, episode.vote_average)

        if conn:
            conn.execute(query, params)
            self.save_playable_media_provider(episode, conn)
            return

        with MoexfilmDbConnector() as conn:
            conn.execute(query, params)
            self.save_playable_media_provider(episode, conn)
