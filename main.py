from typing import List

from pygit2 import *

from dtos.TeamInfoDto import TeamInfoDto
from resolvers.CommitResolver import get_commits_data
from resolvers.LanguagesLocResolver import get_languages_data


def get_repo_info(repo: Repository, repo_path: str, branch_name: str) -> TeamInfoDto:

    commits = get_commits_data(repo, branch_name)
    languages = get_languages_data(repo_path)

    return TeamInfoDto(commits, languages)


some_urls = ["https://github.com/DanArmor/RPN_complex_C", "https://gitlab.com/DanArmor/back.git"]

author = "DanArmor"
repo_name = "back"

teams: List[TeamInfoDto] = []

num = 0
for url in some_urls:

    cloned_repo: Repository = clone_repository(url, "/repo_" + str(num))
    repo_path = cloned_repo.path.replace("/.git/", "")

    # для нумерации папок с репозиториями, возможно нужно поменять на "автор_репозиторий"
    num += 1

    if cloned_repo.branches.get("main") is not None:
        teams.append(get_repo_info(cloned_repo, repo_path, "main"))
    elif cloned_repo.branches.get("master") is not None:
        teams.append(get_repo_info(cloned_repo, repo_path, "master"))
    else:
        print("Нет главной ветки или она называется как хуйня (как типо main, только не main) - " + cloned_repo.path)
