from typing import List


class TeamReposDto:

    def __init__(self, team_id: int, reps: List[str]) -> None:
        self.team_id = team_id
        self.reps = reps
