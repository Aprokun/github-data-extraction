from marshmallow import Schema, fields

from converters.TeamInfoDtoSchema import TeamInfoDtoSchema


class HacktonInfoDtoSchema(Schema):
    common_commits_count = fields.Int()
    common_loc_count = fields.Int()
    teams = fields.Nested(TeamInfoDtoSchema, many=True)
