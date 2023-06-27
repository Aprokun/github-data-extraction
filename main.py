from pygit2 import *

from resolvers.CommitResolver import get_commits_data

some_urls = ["https://github.com/DanArmor/RPN_complex_C", "https://gitlab.com/DanArmor/back.git"]


def get_repo(author: str, repo_name: str) -> Repository:
    return clone_repository("https://gitlab.com/" + author + "/" + repo_name + ".git", "/" + author + "_" + repo_name)


author = "DanArmor"
repo_name = "back"

num = 0
for url in some_urls:

    cloned_repo: Repository = clone_repository(url, "/repo_" + str(num))
    num += 1

    if cloned_repo.branches.get("main") is not None:
        team_info = get_commits_data(cloned_repo, "main")
        loc = get_languages_data(cloned_repo.path.replace("/.git/", ""))
        print(team_info.commits, team_info.common_commit_amount)
    elif cloned_repo.branches.get("master") is not None:
        team_info = get_commits_data(cloned_repo, "master")
        loc = get_languages_data(cloned_repo.path)
    else:
        print("Нет главной ветки или она называется как хуйня (как типо main, только не main)")
