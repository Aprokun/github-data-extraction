import json
import subprocess
from typing import List, Dict

from dtos.LanguageDto import LanguageDto


def count_languages_lines(repo_path: str):

    command = ['cloc', '--json', repo_path]
    output = subprocess.check_output(command).decode('utf-8')
    result = json.loads(output)

    return result


def get_languages_data(repo_path: str) -> List[LanguageDto]:

    languages: List[LanguageDto] = []

    languages_lines: Dict = count_languages_lines(repo_path)

    for key in languages_lines.keys():

        if key == 'header' or key == 'SUM':
            continue

        languages.append(LanguageDto(key, languages_lines[key]['code']))

    return languages
