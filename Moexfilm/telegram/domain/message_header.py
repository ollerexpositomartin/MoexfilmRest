import datetime
from dataclasses import dataclass


@dataclass
class MessageHeader:
    title: str
    release_date: str

    def _get_release_date(self,text) -> str:
        pass
