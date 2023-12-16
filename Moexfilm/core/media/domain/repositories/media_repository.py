from Moexfilm.core.media.domain.models import Media, PlayableMedia
from Moexfilm.core.media.domain.repositories.moexfilm_connector import MoexfilmConnector
from abc import ABC, abstractmethod


# cambiar connector de carpeta ???

class MediaRepository(ABC):

    @abstractmethod
    def _save_media(self, media: Media, conn: MoexfilmConnector = None):
        pass

    @abstractmethod
    def _save_genres(self, media: Media, conn: MoexfilmConnector = None):
        pass

    @abstractmethod
    def save_playable_media_provider(self, media: PlayableMedia, conn: MoexfilmConnector = None):
        pass

    @abstractmethod
    def _get_all_media(self):
        pass

    @abstractmethod
    def _search_media(self, title: str):
        pass

    @abstractmethod
    def _delete_media(self, id: str):
        pass
