
usuarios = [
    {
        "id": 1,
        "email": "luis@example.com",
        "password": "Luis1234",
        "nombre": "Luis",
        "apellido": "Quintana",
        "rol": "admin"
    }
]

def buscar_usuario_por_email_y_password(email: str, password: str):
    for usuario in usuarios:
        if usuario["email"] == email and usuario["password"] == password:
            return usuario
    return None