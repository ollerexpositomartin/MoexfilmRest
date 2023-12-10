from Moexfilm.core.media.domain.models.episode import Episode
from Moexfilm.core.media.domain.models.season import Season
from Moexfilm.core.media.domain.models.media_search_params import MediaSearchParams
from Moexfilm.core.media.domain.models.media_tmdb import MediaTmdb


class TmdbRepository:

    def search_media(self, params: MediaSearchParams) -> MediaTmdb:
        pass

    def search_season(self, tv_id: int, n_season: int) -> Season:
        pass

    def search_episode(self, tv_id: int, n_season: int, n_episode: int) -> Episode:
        pass

    def search_logo(self):
        pass
