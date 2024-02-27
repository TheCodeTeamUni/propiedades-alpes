from propiedadesalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from propiedadesalpes.seedwork.aplicacion.queries import ejecutar_query as query
from propiedadesalpes.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades
from dataclasses import dataclass
from .base import ReservaQueryBaseHandler
from propiedadesalpes.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
import uuid

@dataclass
class ObtenerReserva(Query):
    id: str

class ObtenerReservaHandler(ReservaQueryBaseHandler):

    def handle(self, query: ObtenerReserva) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        propiedad =  self.fabrica_vuelos.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorPropiedad())
        return QueryResultado(resultado=propiedad)

@query.register(ObtenerReserva)
def ejecutar_query_obtener_propiedad(query: ObtenerReserva):
    handler = ObtenerReservaHandler()
    return handler.handle(query)