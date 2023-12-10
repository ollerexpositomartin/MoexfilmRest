import re
from dataclasses import dataclass

DATE_REGEX = "\\(\\d{4}\\)"
TITLE_REGEX = "[A-Za-z ]+"


class MessageHeader:
    title: str
    release_date: str

    def __init__(self, text: str):
        title_match = re.search(TITLE_REGEX, text)
        date_match = re.search(DATE_REGEX, text)

        if not title_match:
            raise Exception("MessageHeader[Title Not Found]")

        self.title = title_match[0].strip()

        if date_match:
            self.release_date = date_match[0].replace("(", "").replace(")", "")
