from datetime import datetime
from typing import List

from pygit2 import GIT_SORT_TIME, Repository, Oid, Commit

from dtos.CommitTimeDto import CommitTimeDto
from dtos.TeamInfoDto import TeamInfoDto


def get_commits_data(repo: Repository, branch_name: str) -> TeamInfoDto:

    commits: List[CommitTimeDto] = []

    if repo.branches.local.get(branch_name) is not None:
        for commit in repo.walk(repo.branches.local.get(branch_name).target, GIT_SORT_TIME):

            commit_info = get_commit_info(repo, commit)
            commits.append(commit_info)

    return TeamInfoDto(len(commits), commits)


# Размер коммита определён как сумма из добавленных строк и удалённых строк
def count_commit_size(repo: Repository, commit_id: Oid) -> int:

    commit = repo.get(commit_id)

    lines_added = 0
    lines_deleted = 0

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