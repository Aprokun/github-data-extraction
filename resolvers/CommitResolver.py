from datetime import datetime
from typing import List, Iterator

from pygit2 import GIT_SORT_TIME, Repository, Oid, Commit, DiffDelta

from dtos.CommitTimeDto import CommitTimeDto


def get_commits_data(repo: Repository, branch_name: str) -> List[CommitTimeDto]:

    commits: List[CommitTimeDto] = []

    if repo.branches.local.get(branch_name) is not None:
        for commit in repo.walk(repo.branches.local.get(branch_name).target, GIT_SORT_TIME):
            commit_info = get_commit_info(repo, commit)
            commits.append(commit_info)

    return commits


def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)


# Размер коммита определён как сумма из добавленных строк и удалённых строк
def count_commit_size(repo: Repository, commit_id: Oid) -> int:
    commit: Commit = repo.get(commit_id)

    lines_added = 0
    lines_deleted = 0

    if len(commit.parents) == 0:

        changed_files: Iterator[DiffDelta] = commit.tree.diff_to_tree().deltas

        lines = 0

        # Если нет родительских коммитов, то считаем все содержимое коммита добавленным
        for delta in changed_files:
            path = repo.path.replace(".git/", "") + delta.new_file.path
            if path.find(".ico") == -1 and path.find(".png") == -1 and path.find(".jpg") == -1:
                lines += count_lines(path)

        return lines

    else:

        for parent in commit.parents:
            diff = repo.diff(parent.tree, commit.tree)

            for patch in diff:
                lines_added += patch.line_stats[1]
                lines_deleted += patch.line_stats[2]

    return lines_added + lines_deleted


def get_commit_info(repo: Repository, commit: Commit) -> CommitTimeDto:
    datetime_string = datetime.utcfromtimestamp(commit.commit_time).strftime('%Y-%m-%d %H:%M:%S')
    size = count_commit_size(repo, commit.id)

    return CommitTimeDto(size, datetime_string)
