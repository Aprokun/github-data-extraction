from marshmallow import Schema, fields


class LanguageDtoSchema(Schema):
    language = fields.Str()
    loc = fields.Int()


class CommitTimeDtoSchema(Schema):
    size = fields.Int()
    datetime = fields.Str()


class RepositoryInfoDtoSchema(Schema):
    commits = fields.Nested(CommitTimeDtoSchema, many=True)
    languages = fields.Nested(LanguageDtoSchema, many=True)


class TeamInfoDtoSchema(Schema):
    team_id = fields.Int()
    repositories = fields.Nested(RepositoryInfoDtoSchema, many=True)
