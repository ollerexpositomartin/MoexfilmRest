from Moexfilm.core.media.domain.models import Media, Movie, TvShow, Season, Episode, MediaType, PlayableMedia
from Moexfilm.core.media.infrastructure.database import MoexfilmDbConnector
from Moexfilm.core.media.domain.repositories import MediaRepository, MoexfilmConnector


class MediaRepositoryImpl(MediaRepository):

    def _save_media(self, media: Media, conn: MoexfilmConnector = None):
        table = "movie" if media.type == MediaType.MOVIE else "tv_show"
        query = f"""
             INSERT INTO public.{table} (tmdb_id,title,overview,backdrop_path
                        ,popularity,poster_path,release_date,vote_average) 
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s);
            """
        params = (media.tmdb_id, media.title, media.overview, media.backdrop_path, media.popularity,
                  media.poster_path, media.release_date, media.vote_average)

        if conn:
            conn.execute(query, params)
            self._save_genres(media, conn)
            return

        with MoexfilmDbConnector() as moex_conn:
            moex_conn.execute(query, params)
            self._save_genres(media, conn)
            moex_conn.end()

    def save_playable_media_provider(self, media: PlayableMedia, conn: MoexfilmDbConnector = None):
        query: str = """ INSERT INTO public.playable_media_provider (tmdb_id, id, provider)
            VALUES (%s,%s,%s);"""
        params = (media.tmdb_id, media.id, media.provider.name)
        if conn:
            conn.execute(query, params)
            return

        with MoexfilmDbConnector() as moex_conn:
            moex_conn.execute(query, params)

    def _save_genres(self, media: Media, conn: MoexfilmConnector = None):
        query: str = f"""INSERT INTO public.media_genre (id, genre_id) 
            VALUES {', '.join(f'({media.tmdb_id}, {genre})' for genre in media.genre_ids)}"""
        if conn:
            conn.execute(query)
            return

        with MoexfilmDbConnector() as moex_conn:
            moex_conn.execute(query)

    def _get_all_media(self):
        pass

    def _search_media(self, title: str):
        raise Exception("Not implemented")

    def _delete_media(self, id: str):
        raise Exception("Not implemented")
