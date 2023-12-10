from datetime import date, datetime

DATE_FORMAT = "%Y-%m-%d"


def get_date(str_date: str) -> date:
    return datetime.strptime(str_date, DATE_FORMAT).date()


def get_str_of_date(datep: date) -> str:
    return datep.strftime(DATE_FORMAT)
