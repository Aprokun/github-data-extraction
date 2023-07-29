import os

from typing import List

from pygit2 import Repository, clone_repository

from converters.TeamReposDtoSchema import TeamReposDtoSchema
from dtos.RepositoryInfoDto import RepositoryInfoDto
from dtos.TeamReposDto import TeamReposDto
from resolvers.HahatonResolver import get_repo_info


def read_urls(file_name: str) -> List[TeamReposDto]:

    with open(file_name, "r") as f:
        json = f.read()
        team_repo_schema = TeamReposDtoSchema(many=True)
        return team_repo_schema.loads(json)


def get_team_repos_info(repository_urls: List[str]) -> List[RepositoryInfoDto]:

    repos: List[RepositoryInfoDto] = []

    for repo_url in repository_urls:

        if "github" not in repo_url and "gitlab" not in repo_url:
            continue

        repo_name = repo_url.split("/")[-1]
        
        cloned_repo: Repository = clone_repository(repo_url, os.path.join(os.getcwd(), "repos", "repo_" + repo_name))
        repo_path: str = cloned_repo.path.replace("/.git/", "")

        main_branch_name = "main" if cloned_repo.branches.get("main") else "master"

        url: RepositoryInfoDto = get_repo_info(cloned_repo, repo_path, main_branch_name)

        repos.append(url)

    return repos
