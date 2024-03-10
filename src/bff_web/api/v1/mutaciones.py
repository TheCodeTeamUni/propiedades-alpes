import logging
import strawberry
import requests
import typing
import uuid

from strawberry.types import Info
from bff_web import utils
from bff_web.despachadores import Despachador

from .esquemas import *


LOCALIZACION_HOST = os.getenv("LOCALIZACION_ADDRES", default="localhost")


@strawberry.type
class Mutation:

    @strawberry.mutation
    def crear_localizacion(self, id_propiedad: str, latitud: float, longitud: float, info: Info) -> PropiedadRespuesta:

        try:
            logging.info(
                f"ID Propiedad: {id_propiedad}, latitud: {latitud}, longitud: {longitud}")
            payload = dict(
                id_propiedad=id_propiedad,
                latitud=latitud,
                longitud=longitud
            )

            resultado = requests.post(
                f'http://{LOCALIZACION_HOST}:8002/agregar-localizacion', json=payload)

            return PropiedadRespuesta(mensaje="Localización agregada", codigo=resultado.status_code)

        except Exception as e:
            logging.error(f"Error al crear localización: {e}")
            return PropiedadRespuesta(mensaje="Error al agregar localización", codigo=500)
