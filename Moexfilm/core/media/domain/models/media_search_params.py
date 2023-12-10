from dataclasses import dataclass
from Moexfilm.core.media.domain.models.media_type import MediaType


@dataclass
class MediaSearchParams:
    title: str | None
    release_date: str | None
    season: int | None
    episode: int | None
    type: MediaType
