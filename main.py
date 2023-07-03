import sys
from typing import List

from converters.HackatonInfoDtoSchema import HacktonInfoDtoSchema
from converters.TeamInfoDtoSchema import TeamInfoDtoSchema
from dtos.TeamInfoDto import TeamInfoDto
from dtos.TeamReposDto import TeamReposDto
from resolvers.HahatonResolver import get_hackaton_info_dto
from utils import get_team_repos_info, read_urls

# Ну я думаю понятно, что тут из параметров командной строки
teams: List[TeamReposDto] = read_urls(sys.argv[1])

teams_info: List[TeamInfoDto] = []

for team in teams:
    repos = get_team_repos_info(team.reps)
    teams_info.append(TeamInfoDto(team.team_id, repos))

hackaton = get_hackaton_info_dto(teams_info)

hackaton_info_schema = HacktonInfoDtoSchema()
team_info_schema = TeamInfoDtoSchema()

print(hackaton_info_schema.dumps(hackaton))

# for team in teams:
#     print(team_info_schema.dumps(team))
