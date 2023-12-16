from abc import ABC, abstractmethod
from typing import List
from Moexfilm.core.media.domain.models import Episode, Season, TvShow


class TvShowRepository(ABC):

    @abstractmethod
    def save_tv_show(self, tv_show: TvShow):
        pass

    @abstractmethod
    def save_season(self, season: Season, conn=None):
        pass

    @abstractmethod
    def save_episode(self, episode: Episode, conn=None):
        pass

    @abstractmethod
    def get_all_tv_shows(self) -> List[TvShow]:
        pass

    @abstractmethod
    def get_all_seasons(self, tv_show_id) -> List[Season]:
        pass

    @abstractmethod
    def get_all_episodes(self, season_id) -> List[Episode]:
        pass
