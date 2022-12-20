# from datetime import datetime

from app.models.database import database
from app.models.sensors import sensors_table
from app.models.users import users_table
# from app.schemas import sensors as sensors_schema
from sqlalchemy import desc, func, select


async def get_sensor(post_id: int):
    query = (
        select(
            [
                sensors_table.c.id,
                sensors_table.c.created_at,
                sensors_table.c.tension,
                sensors_table.c.temperature,
                sensors_table.c.water_level,
                sensors_table.c.continuity,
                sensors_table.c.user_id,
                users_table.c.name.label("user_name"),
            ]
        )
        .select_from(sensors_table.join(users_table))
        .where(sensors_table.c.id == post_id)
    )
    return await database.fetch_one(query)


async def get_sensors(page: int):
    max_per_page = 10
    offset1 = (page - 1) * max_per_page
    query = (
        select(
            [
                sensors_table.c.id,
                sensors_table.c.created_at,
                sensors_table.c.tension,
                sensors_table.c.temperature,
                sensors_table.c.water_level,
                sensors_table.c.continuity,
                sensors_table.c.user_id,
                users_table.c.name.label("user_name"),
            ]
        )
        .select_from(sensors_table.join(users_table))
        .order_by(desc(sensors_table.c.created_at))
        .limit(max_per_page)
        .offset(offset1)
    )
    return await database.fetch_all(query)


async def get_sensors_count():
    query = select([func.count()]).select_from(sensors_table)
    return await database.fetch_val(query)

# async def update_post(post_id: int, post: post_schema.PostModel):
#     query = (
#         posts_table.update()
#         .where(posts_table.c.id == post_id)
#         .values(title=post.title, content=post.content)
#     )
#     return await database.execute(query)
