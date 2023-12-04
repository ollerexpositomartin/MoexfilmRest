import re
from Moexfilm.telegram.domain.message_header import MessageHeader

MOVIE_TITLE_REGEX = "^[A-Za-z ]+ ?\\(\\d{4}\\)$"


class MessageMovieHeader(MessageHeader):

    def __init__(self, text: str):
        self.release_date = self._get_release_date(text)
        self.title = self._get_title(text)

    def _get_title(self, text: str):
        if bool(re.search(MOVIE_TITLE_REGEX, text)):
            return text.replace(f"({self.release_date})", "")
        raise Exception("Incorrect format title")
