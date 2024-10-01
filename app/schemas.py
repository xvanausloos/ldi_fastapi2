# Use Pydantic schemas to validate and serialize data. Create these schemas in schemas.py.
import datetime

from pydantic import BaseModel


class PositionBase(BaseModel):
    vessel_id: int
    received_dt_utc: datetime.datetime
    position_lat: float
    position_lon: float


class PositionCreate(PositionBase):
    pass


class Position(PositionBase):
    id: int

    class Config:
        orm_mode = True
