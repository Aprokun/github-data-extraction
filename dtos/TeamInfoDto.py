from typing import List

from dtos.RepositoryInfoDto import RepositoryInfoDto


class TeamInfoDto:

    def __init__(self, team_id: int, repositories: List[RepositoryInfoDto]) -> None:
        self.team_id = team_id
        self.repositories = repositories
