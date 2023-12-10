import re
from Moexfilm.telegram.domain import MessageHeader

SEASON_EPISODE_REGEX = "s?(\\d+)[ex](\\d+)"


class MessageTvShowHeader(MessageHeader):
    season: int
    episode: int

    def __init__(self, text: str):
        super().__init__(text)
        season_episode_match = re.search(SEASON_EPISODE_REGEX, text)
        self.season = season_episode_match[1]
        self.episode = season_episode_match[2]
