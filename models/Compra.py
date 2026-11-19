from pydantic import BaseModel

class Compra(BaseModel):
  ordenDeCompra: str
  idSesion: str
  monto: int
  urlRetorno: str