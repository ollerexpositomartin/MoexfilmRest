from abc import ABC, abstractmethod
from Moexfilm.core.media.domain.models import Movie


class MovieRepository(ABC):

    @abstractmethod
    def save_movie(self, movie: Movie):
        pass
