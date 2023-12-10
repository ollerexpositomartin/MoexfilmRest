from Moexfilm.core.media.domain.models.provider import Provider
from dataclasses import dataclass


@dataclass
class PlayableMedia:
    tmdb_id: int = None
    id: str = None
    provider: Provider = None
