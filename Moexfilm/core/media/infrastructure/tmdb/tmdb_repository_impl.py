import logging

from Moexfilm.core.media.domain.repositories import TmdbRepository
from Moexfilm.core.media.domain.models import MediaSearchParams, MediaTmdb, SeasonTmdb, EpisodeTmdb
from Moexfilm import application_context
import requests

TMDB_BASE_URL = "https://api.themoviedb.org/3"

AUTH = f"?api_key={application_context.config.TMDB_API_KEY}"

LANGUAGE = "&language=es-ES"

MOVIE_AND_TV_SHOW_URL = TMDB_BASE_URL + "/search/{0}" + AUTH + "&query={1}&year={2}" + LANGUAGE

SEASON = "/tv/{0}/season/{1}"

SEASON_URL = TMDB_BASE_URL + SEASON + AUTH + LANGUAGE

EPISODE_URL = TMDB_BASE_URL + SEASON + "/episode/{2}" + AUTH + LANGUAGE


class TmdbRepositoryImpl(TmdbRepository):

    def search_media(self, params: MediaSearchParams) -> MediaTmdb | None:
        response = requests.get(
            MOVIE_AND_TV_SHOW_URL.format(params.type.value, params.title, params.release_date)
        )
        if response.status_code == 200:
            result = response.json()['results'][0]

            if not result:
                logging.warning(f"Not found {params.title} ({params.release_date}) 👻")
                return None

            return MediaTmdb.from_dict(result)
        else:
            raise Exception("Repository[badResponse]")

    def search_season(self, tv_id: int, n_season: int) -> SeasonTmdb:
        response = requests.get(
            SEASON_URL.format(tv_id, n_season)
        )

        if response.status_code == 200:
            result = response.json()

            return SeasonTmdb.from_dict(result)

        else:
            raise Exception("Repository[badResponse]")

    def search_episode(self, tv_id, n_season, n_episode):
        response = requests.get(
            EPISODE_URL.format(tv_id, n_season, n_episode)
        )

        if response.status_code == 200:
            result = response.json()
            return EpisodeTmdb.from_dict(result)

        else:
            raise Exception("Repository[badResponse]")

    def search_logo(self):
        pass
