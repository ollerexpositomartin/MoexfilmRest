from Moexfilm.core.media.application.tv_show_store_service import TvShowStoreService
from Moexfilm.core.media.domain.models import TvShow, Season, Episode
from Moexfilm.core.media.domain.repositories import TvShowRepository


class TvShowService:

    def __init__(self, tv_show_repository: TvShowRepository):
        self.tv_show_repository = tv_show_repository
        self.cache: TvShowStoreService = TvShowStoreService(tv_show_repository)

    def save_tv_show(self, tv_show: TvShow):
        self.tv_show_repository.save_tv_show(tv_show)

    def save_season(self, season: Season):
        self.tv_show_repository.save_season(season)

    def save_episode(self, episode: Episode):
        self.tv_show_repository.save_episode(episode)
