from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import authRoutes, testRoutes, juegosRoutes, comprasRoutes

app = FastAPI(
    title="Mi ejemplo de API",
    description="Ejemplo de FastAPI",
    version="1.0.0"
)


# --- Configuración de CORS ---
origins = [
    "http://localhost:5173",
    "https://miapp.com"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Incluir rutas ---
app.include_router(authRoutes.router)
app.include_router(testRoutes.router)
app.include_router(juegosRoutes.router)
app.include_router(comprasRoutes.router)
