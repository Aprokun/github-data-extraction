from typing import List

from dtos.CommitTimeDto import CommitTimeDto


class CommitsInfoDto:

    def __init__(self, commits: List[CommitTimeDto]) -> None:
        self.commits: List[CommitTimeDto] = commits
        self.count = len(commits)
