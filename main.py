from pygit2 import *


def get_commits_amount(branch_name: str):
    commits_count = 0

    if cloned_repo.branches.local.get(branch_name) is not None:
        for _ in cloned_repo.walk(cloned_repo.branches.local.get(branch_name).target, GIT_SORT_TIME):
            commits_count += 1

    return commits_count


author = "DanArmor"
repo_name = "back"

cloned_repo: Repository \
    = clone_repository("https://gitlab.com/" + author + "/" + repo_name + ".git", "/" + author + "_" + repo_name)

master_count = get_commits_amount("master")
main_count = get_commits_amount("main")
develop_count = get_commits_amount("develop")

print(master_count, main_count, develop_count)
