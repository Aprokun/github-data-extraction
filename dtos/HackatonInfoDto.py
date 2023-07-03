from typing import List, Dict

from dtos.TeamInfoDto import TeamInfoDto


class HackatonInfoDto:

    def __init__(
        self, common_language_stats: Dict[str, int], common_commits_count: int,
        common_loc_count: int, teams: List[TeamInfoDto]
    ) -> None:
        self.common_language_stats: Dict[str, int] = common_language_stats
        self.common_commits_count: int = common_commits_count
        self.common_loc_count: int = common_loc_count
        self.teams: List[TeamInfoDto] = teams
