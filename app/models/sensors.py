import sqlalchemy

from .users import users_table

metadata = sqlalchemy.MetaData()

sensors_table = sqlalchemy.Table(
    "sensors",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey(users_table.c.id)),
    sqlalchemy.Column("tension", sqlalchemy.Integer),
    sqlalchemy.Column("temperature", sqlalchemy.Integer),
    sqlalchemy.Column("water_level", sqlalchemy.Integer),
    sqlalchemy.Column("continuity", sqlalchemy.Integer),
)
