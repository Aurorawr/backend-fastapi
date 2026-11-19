from fastapi import APIRouter, Depends, HTTPException, status
from models.Compra import Compra
from models.TokenWebpay import TokenWebpay
from services.webpayService import generar_link_de_pago, confirmar_pago

router = APIRouter(
    prefix="/api/v1/compras",
    tags=["Compras"],
)

@router.post("/generar-link-pago")
def crear_link_de_pago(compra: Compra):
    return generar_link_de_pago(compra.ordenDeCompra, compra.idSesion, compra.monto, compra.urlRetorno)

@router.post("/confirmar-pago")
def confirmar_pago_realizado(token_data: TokenWebpay):
    return confirmar_pago(token_data.tokenWebpay)

    