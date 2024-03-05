import asyncio

from fastapi import FastAPI
from pydantic import BaseSettings
from typing import Any


from .comandos import AgregarPlano, ComandoAgregarPlano
from .consumidores import suscribirse_a_topico
from .despachadores import Despachador
from . import utils

class Config(BaseSettings):
    APP_VERSION: str = "1"

settings = Config()
app_configs: dict[str, Any] = {"title": "Planos PropiedadesAlpes"}

app = FastAPI(**app_configs)
tasks = list()

@app.on_event("startup")
async def app_startup():
    global tasks
    task1 = asyncio.ensure_future(suscribirse_a_topico("comando-agregar-plano", "sub-com-agregar-plano", ComandoAgregarPlano))
    tasks.append(task1)

@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()


@app.get("/agregar-plano", include_in_schema=False)
async def prueba_agregar_contrato() -> dict[str, str]:
    payload = AgregarPlano(
        id_propiedad = "15AA22C",
        dimensiones = "150x30",
        descripcion = "Propiedad a la afueras de la ciudad, con 4 habitaciones dos baños, cocina y sala",
        plano = "http://propiedadesalpes.com/plano_15AA22C",
    )

    comando = ComandoAgregarPlano(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=AgregarPlano.__name__,
        data = payload
    )

    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-agregar-plano")
    return {"status": "ok"}