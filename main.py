"""
Gestion De Pacientes Para Clinica Dental Con Citas Y - API REST
Generado por ATLAS CORE
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from database import init_db
from auth import router as auth_router
from routes.items import router as items_router
from routes.export import router as export_router

app = FastAPI(
    title="Gestion De Pacientes Para Clinica Dental Con Citas Y",
    description="API REST con autenticación JWT",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "healthy"}

# Routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(items_router, prefix="/items", tags=["items"])
app.include_router(export_router, prefix="/export", tags=["export"])

# Servir frontend en / y /app
@app.get("/")
@app.get("/app")
def serve_frontend():
    return FileResponse("frontend/index.html")
