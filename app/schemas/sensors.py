from datetime import datetime

from pydantic import BaseModel


class SensorModel(BaseModel):
    id: int
    tension: int
    temperature: int
    water_level: int
    continuity: int
    created_at: datetime
