import typing
import strawberry
import requests
import os


LOCALIZACION_HOST = os.getenv("LOCALIZACION_ADDRES", default="localhost")


def obtener_localizaciones(root) -> typing.List["Propiedad"]:
    propiedades_json = requests.get(
        f'http://{LOCALIZACION_HOST}:8002/obtener-localizaciones').json()
    propiedades = []

    for propiedad in propiedades_json:
        propiedades.append(
            Propiedad(
                id=propiedad.get('id'),
                id_propiedad=propiedad.get('id_propiedad'),
                latitud=propiedad.get('latitud'),
                longitud=propiedad.get('longitud'),
                created_at=propiedad.get('created_at')
            )
        )

    return propiedades


@strawberry.type
class Propiedad:
    id: int
    id_propiedad: str
    latitud: float
    longitud: float
    created_at: str


@strawberry.type
class PropiedadRespuesta:
    mensaje: str
    codigo: int
