from typing import List

from Moexfilm.core.media.domain.models import Episode, Season, TvShow
from Moexfilm.core.media.domain.repositories import MediaRepository


class TvShowRepository:

    def save_tv_show(self, tv_show: TvShow):
        pass

    def save_season(self, season: Season, conn=None):
        pass

    def save_episode(self, episode: Episode, conn=None):
        pass

    def get_all_tv_shows(self) -> List[TvShow]:
        pass

    def get_all_seasons(self, tv_show_id) -> List[Season]:
        pass

    def get_all_episodes(self, season_id) -> List[Episode]:
        pass
