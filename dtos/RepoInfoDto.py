from typing import List

from LanguagesInfoDto import LanguagesInfoDto


class RepoInfoDto:

    def __init__(self, commonCommitAmount: int, commonLineAmount: int, languages: List[LanguagesInfoDto]) -> None:
        self.commonCommitAmount = commonCommitAmount
        self.commonLineAmount = commonLineAmount
        self.languages = languages

