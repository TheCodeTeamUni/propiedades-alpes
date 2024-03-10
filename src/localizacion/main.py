import asyncio
from pydantic import BaseSettings
from typing import Any
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .comandos import AgregarUbicacion, ComandoAgregarUbicacion
from .consumidores import suscribirse_a_topico
from .despachadores import Despachador
from . import utils
from sqlalchemy import DateTime, func
from typing import List
from fastapi import Depends
from fastapi import Depends
from sqlalchemy.orm import Session



Base = declarative_base()
engine = create_engine('sqlite:///propiedades.db', connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Propiedad(Base):
    __tablename__ = "propiedades"
    id = Column(Integer, primary_key=True, index=True)
    id_propiedad = Column(String, index=True)
    latitud = Column(Float)
    longitud = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

# Función para crear las tablas
def create_tables():
    Base.metadata.create_all(bind=engine)

class Config(BaseSettings):
    APP_VERSION: str = "1"

settings = Config()
app_configs: dict[str, Any] = {"title": "Localizacion PropiedadesAlpes"}

app = FastAPI(**app_configs)
tasks = list()

create_tables()


@app.on_event("startup")
async def app_startup():
    global tasks
    task1 = asyncio.ensure_future(suscribirse_a_topico("comando-agregar-ubicacion", "sub-com-agregar-ubicacion", ComandoAgregarUbicacion))
    tasks.append(task1)

@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()


@app.get("/agregar-ubicacion", include_in_schema=False)
async def prueba_agregar_contrato() -> dict[str, str]:
    payload = AgregarUbicacion(
        id_propiedad = "15AA22C",
        latitud = 2.25,
        longitud = 3.56
    )

    comando = ComandoAgregarUbicacion(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=AgregarUbicacion.__name__,
        data = payload
    )

    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-agregar-ubicacion")
    return {"status": "ok"}


@app.post("/agregar-localizacion", response_model=dict)
async def agregar_propiedad(propiedad_data: dict):
    try:
        id_propiedad = propiedad_data.get("id_propiedad")
        latitud = propiedad_data.get("latitud")
        longitud = propiedad_data.get("longitud")

        if not all([id_propiedad, latitud, longitud]):
            raise HTTPException(status_code=422, detail="Todos los campos son obligatorios")

        # Crear instancia de la clase Propiedad
        propiedad = Propiedad(id_propiedad=id_propiedad, latitud=latitud, longitud=longitud)

        # Agregar propiedad a la base de datos
        db = SessionLocal()
        db.add(propiedad)
        db.commit()
        db.refresh(propiedad)
        db.close()

        # Puedes agregar aquí cualquier lógica adicional, como publicar un mensaje, etc.

        return {"status": "ok", "message": "Propiedad agregada correctamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/obtener-localizaciones", response_model=list)
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    propiedades = db.query(Propiedad).all()
    return propiedades