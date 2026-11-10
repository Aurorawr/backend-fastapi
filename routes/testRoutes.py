from fastapi import APIRouter, Depends, HTTPException, status

from middlewares.validacion_token import validar_token

router = APIRouter(
    prefix="/api/v1/test",
    tags=["test"],
    dependencies=[Depends(validar_token)],
)

@router.get("")
def test_endpoint():
    return {"message": "Hola hola buenas tardes"}
    