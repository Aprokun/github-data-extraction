from dtos.CommitsInfoDto import CommitsInfoDto
from dtos.LanguagesInfoDto import LanguagesInfoDto


class TeamInfoDto:

    def __init__(self, commits: CommitsInfoDto, languages: LanguagesInfoDto) -> None:
        self.languages = languages
        self.commits = commits
