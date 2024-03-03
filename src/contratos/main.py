import asyncio

from fastapi import FastAPI
from pydantic import BaseSettings
from typing import Any

from .eventos import EventoPago, PagoRevertido, ReservaPagada
from .comandos import AgregarContrato, ComandoAgregarContrato
from .consumidores import suscribirse_a_topico
from .despachadores import Despachador
from . import utils

class Config(BaseSettings):
    APP_VERSION: str = "1"

settings = Config()
app_configs: dict[str, Any] = {"title": "Pagos AeroAlpes"}

app = FastAPI(**app_configs)
tasks = list()

@app.on_event("startup")
async def app_startup():
    global tasks
    task1 = asyncio.ensure_future(suscribirse_a_topico("comando-agregar-contrato", "sub-com-agregar-contrato", ComandoAgregarContrato))
    tasks.append(task1)

@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()


@app.get("/agregar-contrato", include_in_schema=False)
async def prueba_agregar_contrato() -> dict[str, str]:
    payload = AgregarContrato(
        id_propiedad = "15AA22C",
        monto = 120000,
        comprador = "Juan Perez",
        vendedor = "Pedro Perez",
        inquilino = "Carlos Perez",
        arrendador = "Maria Perez"
    )

    comando = ComandoAgregarContrato(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=AgregarContrato.__name__,
        data = payload
    )

    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-agregar-contrato")
    return {"status": "ok"}