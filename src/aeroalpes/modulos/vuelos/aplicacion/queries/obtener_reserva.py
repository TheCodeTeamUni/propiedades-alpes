from aeroalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from aeroalpes.seedwork.aplicacion.queries import ejecutar_query as query
from aeroalpes.modulos.vuelos.infraestructura.repositorios import RepositorioPropiedades
from dataclasses import dataclass
from .base import ReservaQueryBaseHandler
from aeroalpes.modulos.vuelos.aplicacion.mapeadores import MapeadorReserva
import uuid

@dataclass
class ObtenerReserva(Query):
    id: str

class ObtenerReservaHandler(ReservaQueryBaseHandler):

    def handle(self, query: ObtenerReserva) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        reserva =  self.fabrica_vuelos.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorReserva())
        return QueryResultado(resultado=reserva)

@query.register(ObtenerReserva)
def ejecutar_query_obtener_reserva(query: ObtenerReserva):
    handler = ObtenerReservaHandler()
    return handler.handle(query)