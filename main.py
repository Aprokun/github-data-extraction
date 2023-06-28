import sys

from typing import List

from pygit2 import *

from converters.TeamInfoDtoSchema import TeamInfoDtoSchema
from dtos.TeamInfoDto import TeamInfoDto
from resolvers.HahatonResolver import get_repo_info, get_hackaton_info_dto


def read_urls(file_name: str):

    with open(file_name, "r") as f:

        urls = f.readlines()

        # Чтобы без всяких \n и прочего говна
        return [url.strip() for url in urls]


repo_urls = read_urls(sys.argv[1])

teams: List[TeamInfoDto] = []

num = 0
for url in repo_urls:

    cloned_repo: Repository = clone_repository(url, "/repo_" + str(num))
    repo_path = cloned_repo.path.replace("/.git/", "")

    # для нумерации папок с репозиториями (repo_<num>), возможно нужно поменять на "автор_репозиторий"
    num += 1

    if cloned_repo.branches.get("main") is not None:
        teams.append(get_repo_info(cloned_repo, repo_path, "main"))
    elif cloned_repo.branches.get("master") is not None:
        teams.append(get_repo_info(cloned_repo, repo_path, "master"))
    else:
        print("Нет главной ветки или она называется как хуйня (как типо main, только не main) - " + cloned_repo.path)


hackaton = get_hackaton_info_dto(teams)

team_info_schema = TeamInfoDtoSchema()

for team in teams:
    print(team_info_schema.dumps(team))
