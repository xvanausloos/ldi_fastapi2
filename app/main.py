from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/positions/", response_model=list[schemas.Position])
def read_positions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    positions = crud.get_positions(db, skip=skip, limit=limit)
    return positions
