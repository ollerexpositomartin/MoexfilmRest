from Moexfilm.core.media.domain.models import TvShow, Season, Episode, MediaSearchParams
from Moexfilm.core.media.domain.repositories import TvShowRepository
from typing import List, Dict


class TvShowStoreService:
    cache: Dict = {}
    _instance = None

    def __init__(self, tv_show_repository: TvShowRepository):
        self.tv_show_repository = tv_show_repository

    def _load(self):
        self._load_tvs()

    def _load_tvs(self):
        tv_shows: List[TvShow] = self.tv_show_repository.get_all_tv_shows()
        for tv_show in tv_shows:
            self.cache[f"{tv_show.title}#{tv_show.release_date.year}"] = tv_show
            seasons: List[Season] = self._load_seasons(tv_show)
            tv_show.seasons.extend(seasons)

    def _load_seasons(self, tv_show: TvShow) -> List[Season]:
        seasons: List[Season] = self.tv_show_repository.get_all_seasons(tv_show.tmdb_id)
        for season in seasons:
            season.episodes.extend(self._load_episodes(season))
        return seasons

    def _load_episodes(self, season: Season) -> List[Episode]:
        return self.tv_show_repository.get_all_episodes(season.tmdb_id)

    def save(self, tv_show: TvShow):
        self.cache[f"{tv_show.title}#{tv_show.release_date.year}"] = tv_show

    def get(self, key: str) -> TvShow | None:
        if not self.cache:
            self._load()
        if self.cache.__contains__(key):
            return self.cache[key]
