from typing import List

from LanguageDto import LanguageDto


class RepoInfoDto:

    def __init__(self, commonCommitAmount: int, commonLineAmount: int, languages: List[LanguageDto]) -> None:
        self.commonCommitAmount = commonCommitAmount
        self.commonLineAmount = commonLineAmount
        self.languages = languages

