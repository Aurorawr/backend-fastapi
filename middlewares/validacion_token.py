from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from config.settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/iniciar-sesion")

def validar_token(token: str = Depends(oauth2_scheme)) -> str:
    try:
        # jwt.decode verifica la firma y automáticamente comprueba la expiración ('exp')
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El token ha expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No se pudieron validar las credenciales",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return payload
