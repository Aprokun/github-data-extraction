from typing import List

from dtos.CommitTimeDto import CommitTimeDto
from dtos.LanguageDto import LanguageDto


class RepositoryInfoDto:

    def __init__(self, commits: List[CommitTimeDto], languages: List[LanguageDto]) -> None:
        self.languages = languages
        self.languages_count = len(languages)
        self.commits = commits
        self.commits_count = len(commits)
