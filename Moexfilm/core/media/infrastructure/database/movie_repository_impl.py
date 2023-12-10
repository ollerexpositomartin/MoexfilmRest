from Moexfilm.core.media.domain.models import Movie
from Moexfilm.core.media.domain.repositories import MovieRepository
from Moexfilm.core.media.infrastructure.database.moexfilm_db_connector import MoexfilmDbConnector
from Moexfilm.core.media.infrastructure.database.media_repository_impl import MediaRepositoryImpl


class MovieRepositoryImpl(MovieRepository, MediaRepositoryImpl):

    def save_movie(self, movie: Movie):
        with MoexfilmDbConnector() as conn:
            self._save_media(movie, conn)
            self.save_playable_media_provider(movie, conn)
