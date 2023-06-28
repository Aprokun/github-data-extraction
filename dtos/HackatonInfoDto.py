from typing import List

from dtos.TeamInfoDto import TeamInfoDto


class HackatonInfoDto:

    def __init__(self, common_commits_count: int, common_loc: int, teams: List[TeamInfoDto]) -> None:
        self.common_commits_count: int = common_commits_count
        self.common_loc: int = common_loc
        self.teams: List[TeamInfoDto] = teams
