import asyncio

from fastapi import FastAPI
from pydantic import BaseSettings
from typing import Any

from .eventos import EventoPago, PagoRevertido, ReservaPagada
from .comandos import AgregarCompania, ComandoAgregarCompania
from .consumidores import suscribirse_a_topico
from .despachadores import Despachador
from . import utils

class Config(BaseSettings):
    APP_VERSION: str = "1"

settings = Config()
app_configs: dict[str, Any] = {"title": "Compania AeroAlpes"}

app = FastAPI(**app_configs)
tasks = list()

@app.on_event("startup")
async def app_startup():
    global tasks
    task1 = asyncio.ensure_future(suscribirse_a_topico("comando-agregar-compania", "sub-com-agregar-compania", ComandoAgregarCompania))
    tasks.append(task1)

@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()


@app.get("/agregar-compania", include_in_schema=False)
async def prueba_agregar_compania() -> dict[str, str]:
    payload = AgregarCompania(
        id_compania = "AA123"
        nombre = "Propiedades Molina"
        telefono = "1234567890"
        direccion_ppal = "Calle 123 45 67"
    )

    comando = ComandoAgregarCompania(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=AgregarCompania.__name__,
        data = payload
    )

    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-agregar-compania")
    return {"status": "ok"}