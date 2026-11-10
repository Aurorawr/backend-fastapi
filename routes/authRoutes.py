from fastapi import APIRouter, HTTPException, status

from models.CredencialesUsuario import CredencialesUsuario
from services.authService import iniciar_sesion

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["auth"],
)

@router.post("/iniciar-sesion")
def iniciar_sesion_usuario(credenciales: CredencialesUsuario):
    try:
        respuesta_login = iniciar_sesion(credenciales.email, credenciales.password)
        return respuesta_login
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
        )
    