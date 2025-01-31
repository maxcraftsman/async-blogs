from fastapi import APIRouter

from app.schemas.sensors import SensorModel
from app.utils import sensors as sensor_utils

router = APIRouter()


# @router.post("/sensors", response_model=SensorModel, status_code=201)
# async def create_post(post: SensorModel, current_user: User = Depends(get_current_user)):
#     post = await sensor_utils.create_post(post, current_user)
#     return post


@router.get("/sensors")
async def get_posts(page: int = 1):
    total_count = await sensor_utils.get_sensors_count()
    posts = await sensor_utils.get_sensors(page)
    return {"total_count": total_count, "results": posts}


@router.get("/sensors/{sensor_id}", response_model=SensorModel)
async def get_post(post_id: int):
    return await sensor_utils.get_sensor(post_id)


# @router.put("/posts/{post_id}", response_model=PostDetailsModel)
# async def update_post(
#     post_id: int, post_data: PostModel, current_user=Depends(get_current_user)
# ):
#     post = await post_utils.get_post(post_id)
#     if post["user_id"] != current_user["id"]:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="You don't have access to modify this post",
#         )
#
#     await post_utils.update_post(post_id=post_id, post=post_data)
#     return await post_utils.get_post(post_id)
