from typing import List

from dtos.CommitTimeDto import CommitTimeDto


class TeamInfoDto:

    def __init__(self, common_commit_amount: int, commits: List[CommitTimeDto]) -> None:
        self.common_commit_amount = common_commit_amount
        self.commits = commits
