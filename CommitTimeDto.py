import datetime


class CommitTimeDto:

    def __init__(self, size: int, _datetime: datetime) -> None:
        self.size = size
        self.datetime = _datetime
