from pydantic import BaseModel

class CredencialesUsuario(BaseModel):
    email: str
    password: str
    