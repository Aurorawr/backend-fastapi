
from repositories.usersRepository import buscar_usuario_por_email_y_password
from utils.jwtUtils import crear_token_jwt


def iniciar_sesion(email: str, password: str):
    usuario = buscar_usuario_por_email_y_password(email, password)
    if usuario is None:
        raise Exception("Credenciales inválidas")
    datos_usuario = {
        "id": usuario["id"],
        "email": usuario["email"],
        "nombre": usuario["nombre"],
        "apellido": usuario["apellido"],
        "rol": usuario["rol"],
    }
    token = crear_token_jwt(data=datos_usuario)
    datos_usuario["token"] = token
    return datos_usuario