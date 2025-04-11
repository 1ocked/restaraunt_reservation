from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Reservation, Table
from app.schemas.schemas import ReservationCreate

router = APIRouter()

@router.post("/reservations/")
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    # Проверка на пересечения брони
    conflicting_reservations = db.query(Reservation).filter(
        Reservation.table_id == reservation.table_id,
        Reservation.reservation_time < reservation.reservation_time + reservation.duration_minutes,
        Reservation.reservation_time + Reservation.duration_minutes > reservation.reservation_time
    ).all()

    if conflicting_reservations:
        raise HTTPException(status_code=400, detail="Table is already reserved for the specified time")

    new_reservation = Reservation(**reservation.dict())
    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)
    return new_reservation
