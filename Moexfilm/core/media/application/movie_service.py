from Moexfilm.core.media.domain.models import Movie
from Moexfilm.core.media.domain.repositories import MovieRepository


class MovieService:

    def __init__(self, movie_repository: MovieRepository):
        self.movie_repository = movie_repository

    def save_movie(self, movie: Movie):
        self.movie_repository.save_movie(movie)
