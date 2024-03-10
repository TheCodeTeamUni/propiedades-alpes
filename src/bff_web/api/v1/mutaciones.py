import logging
import strawberry
import typing
import uuid

from strawberry.types import Info
from bff_web import utils
from bff_web.despachadores import Despachador

from .esquemas import *

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def crear_localizacion(self, id_propiedad: str, latitud: float, longitud: float, info: Info) -> PropiedadRespuesta:
        logging.info(f"ID Propiedad: {id_propiedad}, latitud: {latitud}, longitud: {longitud}")
        payload = dict(
            id_propiedad = id_propiedad,
            latitud = latitud,
            longitud = longitud
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoPropiedad",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "eventos-localizacion", "public/default/eventos-localizacion")
        
        return PropiedadRespuesta(mensaje="Procesando Mensaje", codigo=203)