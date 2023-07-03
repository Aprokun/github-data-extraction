from marshmallow import Schema, fields, post_load

from dtos.TeamReposDto import TeamReposDto


class TeamReposDtoSchema(Schema):
    team_id = fields.Int()
    reps = fields.List(fields.Str())

    @post_load
    def make_team(self, data, **kwargs):
        return TeamReposDto(**data)
