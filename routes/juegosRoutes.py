from fastapi import APIRouter
from services.juegosService import obtener_los_juegos

router = APIRouter(
    prefix="/api/v1/juegos",
    tags=["test"],
)

@router.get("")
def get_juegos():
    return obtener_los_juegos()
    