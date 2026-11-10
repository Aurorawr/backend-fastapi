# API FastAPI con Autenticación JWT

Este repositorio contiene una aplicación backend desarrollada con **FastAPI**, que implementa autenticación mediante **JSON Web Tokens (JWT)** y gestión de configuración con **Pydantic Settings**.

---

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado en tu sistema:
* **Python 3.10** o superior.
* **Pip** (administrador de paquetes de Python).

---

## Configuración del Entorno de Desarrollo

Sigue estos pasos secuenciales para preparar y ejecutar la aplicación en tu máquina local.

### 1. Crear el Entorno Virtual

Abre una terminal en la raíz del proyecto y ejecuta el siguiente comando para crear la carpeta del entorno virtual (`venv`):

```bash
python -m venv venv
```

---

### 2. Activar el Entorno Virtual

Ejecuta el comando correspondiente a tu sistema operativo y shell:

* **Linux / macOS:**
  ```bash
  source venv/bin/activate
  ```

* **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
  *(Si aparece un error sobre políticas de ejecución en PowerShell, ejecuta primero: `Set-ExecutionPolicy -ExecutionPolicy Process -Scope Process`)*

* **Windows (CMD):**
  ```cmd
  venv\Scripts\activate.bat
  ```

> 💡 **Verificación:** Sabrás que el entorno está activo porque verás el prefijo `(venv)` en tu terminal.

---

### 3. Instalar Dependencias

Con el entorno virtual activado, instala todas las librerías necesarias mediante el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### 4. Configurar Variables de Entorno

Crea un archivo llamado `.env` en la raíz del proyecto y agrega las variables requeridas por la aplicación (que también están en el archivo .env.example):

```env
# Clave secreta para firmar tokens (Genera una segura en producción)
SECRET_KEY="tu_clave_secreta_super_segura_aqui"

# Algoritmo de encriptación JWT
ALGORITHM="HS256"

# Tiempo de expiración del token (en minutos)
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Ejecutar la Aplicación

Para iniciar el servidor de desarrollo local con recarga en tiempo real (*hot-reload*):

```bash
uvicorn main:app --reload
```

La API comenzará a responder en: `http://127.0.0.1:8000`

---

## Documentación Interactiva

FastAPI genera documentación interactiva de forma automática. Puedes acceder a ella desde tu navegador mientras la aplicación se esté ejecutando:

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🛑 Salir del Entorno Virtual

Una vez que hayas finalizado tu trabajo, puedes desactivar el entorno virtual ejecutando:

```bash
deactivate
```