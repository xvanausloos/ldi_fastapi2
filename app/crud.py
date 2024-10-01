from sqlalchemy.orm import Session
from . import models, schemas


def get_positions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Position).offset(skip).limit(limit).all()
