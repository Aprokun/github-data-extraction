from pygit2 import *

from resolvers.CommitResolver import get_commits_data


def get_repo(author: str, repo_name: str) -> Repository:
    return clone_repository("https://gitlab.com/" + author + "/" + repo_name + ".git", "/" + author + "_" + repo_name)


author = "DanArmor"
repo_name = "back"

cloned_repo = get_repo(author, repo_name)

if cloned_repo.branches.get("main") is not None:
    team_info = get_commits_data("main")
    print(team_info.commits, team_info.common_commit_amount)
elif cloned_repo.branches.get("master") is not None:
    team_info = get_commits_data("master")
else:
    print("Нет главной ветки или она называется как хуйня (не main)")
