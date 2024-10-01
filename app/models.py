from sqlalchemy import Column, DateTime, Float, Integer, String
from .database import Base


class Vessel(Base):
    __tablename__ = "vessel"
    id = Column(Integer, primary_key=True)
    vessel_name = Column(String)
    vessel_flag = Column(String)
    vessel_imo = Column(String)


class Position(Base):
    __tablename__ = "position"
    id = Column(Integer, primary_key=True)
    vessel_id = Column(Integer)
    received_dt_utc = Column(DateTime)
    position_lat = Column(Float)
    position_lon = Column(Float)


class Point(Base):
    __tablename__ = "point"
    id = Column(Integer, primary_key=True)
    point_name = Column(String)
    point_type = Column(String)
    point_lat = Column(Float)
    point_lon = Column(Float)
