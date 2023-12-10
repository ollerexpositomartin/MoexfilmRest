from Moexfilm.core.media.domain.models import Media, PlayableMedia
from Moexfilm.core.media.domain.repositories.moexfilm_connector import MoexfilmConnector
#cambiar connector de carpeta ???

class MediaRepository:

    def _save_media(self, media: Media, conn: MoexfilmConnector = None):
        pass

    def _save_genres(self,media:Media,conn:MoexfilmConnector = None):
        pass

    def save_playable_media_provider(self, media: PlayableMedia, conn: MoexfilmConnector = None):
        pass

    def _get_all_media(self):
        pass

    def _search_media(self, title: str):
        pass

    def _delete_media(self, id: str):
        pass


