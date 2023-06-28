from typing import List

from pygit2 import Repository

from dtos.HackatonInfoDto import HackatonInfoDto
from dtos.TeamInfoDto import TeamInfoDto
from resolvers.CommitResolver import get_commits_data
from resolvers.LanguagesLocResolver import get_languages_data


def get_repo_info(repo: Repository, repo_path: str, branch_name: str) -> TeamInfoDto:

    commits = get_commits_data(repo, branch_name)
    languages = get_languages_data(repo_path)

    return TeamInfoDto(commits, languages)


def get_hackaton_info_dto(teams: List[TeamInfoDto]) -> HackatonInfoDto:
    common_commits_count = 0
    common_loc_count = 0

    for team in teams:
        common_commits_count += team.commits_count
        common_loc_count += sum([lang.loc for lang in team.languages])

    return HackatonInfoDto(common_commits_count, common_loc_count, teams)