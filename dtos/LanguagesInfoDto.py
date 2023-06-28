from typing import List

from dtos.LanguageDto import LanguageDto


class LanguagesInfoDto:

    def __init__(self, languages: List[LanguageDto]) -> None:
        self.languages: List[LanguageDto] = languages
