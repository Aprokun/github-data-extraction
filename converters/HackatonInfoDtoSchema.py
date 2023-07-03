from marshmallow import Schema, fields

from converters.TeamInfoDtoSchemas import TeamInfoDtoSchema


class HacktonInfoDtoSchema(Schema):
    common_commits_count = fields.Int()
    common_loc_count = fields.Int()
    common_language_stats = fields.Dict(fields.Str(), fields.Int())
    teams = fields.Nested(TeamInfoDtoSchema, many=True)
