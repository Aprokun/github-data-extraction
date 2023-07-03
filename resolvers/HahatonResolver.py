from typing import List, Dict

from pygit2 import Repository

from dtos.HackatonInfoDto import HackatonInfoDto
from dtos.RepositoryInfoDto import RepositoryInfoDto
from dtos.TeamInfoDto import TeamInfoDto
from resolvers.CommitResolver import get_commits_data
from resolvers.LanguagesLocResolver import get_languages_data


def get_repo_info(repo: Repository, repo_path: str, branch_name: str) -> RepositoryInfoDto:
    commits = get_commits_data(repo, branch_name)
    languages = get_languages_data(repo_path)

    return RepositoryInfoDto(commits, languages)


def get_hackaton_info_dto(teams: List[TeamInfoDto]) -> HackatonInfoDto:
    common_commits_count = 0
    common_loc_count = 0
    common_languages_stats: Dict[str, int] = {}

    for team in teams:
        for repo in team.repositories:
            common_commits_count += repo.commits_count
            common_loc_count += sum([lang.loc for lang in repo.languages])
            for lang in repo.languages:
                if lang.language in common_languages_stats:
                    common_languages_stats[lang.language] += lang.loc
                else:
                    common_languages_stats[lang.language] = lang.loc

    return HackatonInfoDto(common_languages_stats, common_commits_count, common_loc_count, teams)
