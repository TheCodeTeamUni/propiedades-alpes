import asyncio
from sse_starlette.sse import EventSourceResponse
from fastapi import FastAPI, Request
from pydantic import BaseSettings
from typing import Any

from .consumidores import suscribirse_a_topico
from .despachadores import Despachador
from . import utils
from .api.v1.router import router as v1


class Config(BaseSettings):
    APP_VERSION: str = "1"


settings = Config()
app_configs: dict[str, Any] = {"title": "BFF-Web Propiedades Alpes"}

app = FastAPI(**app_configs)
tasks = list()
eventos = list()


@app.on_event("startup")
async def app_startup():
    global tasks
    global eventos
    task1 = asyncio.ensure_future(suscribirse_a_topico(
        "eventos-localizacion", "propiedadesalpes-bff", "public/default/eventos-localizacion", eventos=eventos))
    tasks.append(task1)


@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()


@app.get('/stream')
async def stream_mensajes(request: Request):
    def nuevo_evento():
        global eventos
        return {'data': eventos.pop(), 'event': 'NuevoEvento'}

    async def leer_eventos():
        global eventos
        while True:
            # Si el cliente cierra la conexión deja de enviar eventos
            if await request.is_disconnected():
                break

            if len(eventos) > 0:
                yield nuevo_evento()

            await asyncio.sleep(0.1)

    return EventSourceResponse(leer_eventos())


app.include_router(v1, prefix="/v1")
