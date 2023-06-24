from typing import List

from CommitTimeDto import CommitTimeDto


class TeamInfoDto:

    def __init__(self, commonCommitAmount: int, commits: List[CommitTimeDto]) -> None:
        self.commonCommitAmount = commonCommitAmount
        self.commits = commits
