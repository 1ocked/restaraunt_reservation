from fastapi import FastAPI
from app.routers import tables, reservations

app = FastAPI()

app.include_router(tables.router)
app.include_router(reservations.router)

# Подключение маршрутов для API
app.include_router(tables.router, prefix="/tables", tags=["Tables"])
app.include_router(reservations.router, prefix="/reservations", tags=["Reservations"])
