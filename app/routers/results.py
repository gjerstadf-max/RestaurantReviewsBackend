from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, models

router = APIRouter(prefix="/results", tags=["results"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ResultOut)
def create_result(data: schemas.ResultCreate, db: Session = Depends(get_db)):
    result = models.Result(**data.dict())
    db.add(result)
    db.commit()
    db.refresh(result)
    return result

@router.get("/", response_model=list[schemas.ResultOut])
def list_results(db: Session = Depends(get_db)):
    return db.query(models.Result).all()
