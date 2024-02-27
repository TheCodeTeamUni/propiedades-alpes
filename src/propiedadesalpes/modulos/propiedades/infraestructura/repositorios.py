""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from propiedadesalpes.config.db import db
from propiedadesalpes.modulos.propiedades.dominio.repositorios import RepositorioPropiedades, RepositorioProveedores
from propiedadesalpes.modulos.propiedades.dominio.objetos_valor import NombrePropiedades, Odo, Leg, Segmento, Itinerario, CodigoIATA
from propiedadesalpes.modulos.propiedades.dominio.entidades import Proveedor, Propiedadespuerto, Propiedad
from propiedadesalpes.modulos.propiedades.dominio.fabricas import FabricaPropiedades
from .dto import Reserva as ReservaDTO
from .mapeadores import MapeadorReserva
from uuid import UUID

class RepositorioProveedoresSQLite(RepositorioProveedores):

    def obtener_por_id(self, id: UUID) -> Propiedad:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Propiedad]:
        origen=Propiedadespuerto(codigo="CPT", nombre="Cape Town International")
        destino=Propiedadespuerto(codigo="JFK", nombre="JFK International Airport")
        legs=[Leg(origen=origen, destino=destino)]
        segmentos = [Segmento(legs)]
        odos=[Odo(segmentos=segmentos)]

        proveedor = Proveedor(codigo=CodigoIATA(codigo="AV"), nombre=NombrePropiedades(nombre= "Avianca"))
        proveedor.itinerarios = [Itinerario(odos=odos, proveedor=proveedor)]
        return [proveedor]

    def agregar(self, entity: Propiedad):
        # TODO
        raise NotImplementedError

    def actualizar(self, entity: Propiedad):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError


class RepositorioPropiedadesSQLite(RepositorioPropiedades):

    def __init__(self):
        self._fabrica_vuelos: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos

    def obtener_por_id(self, id: UUID) -> Propiedad:
        propiedad_dto = db.session.query(ReservaDTO).filter_by(id=str(id)).one()
        return self.fabrica_vuelos.crear_objeto(propiedad_dto, MapeadorReserva())

    def obtener_todos(self) -> list[Propiedad]:
        # TODO
        raise NotImplementedError

    def agregar(self, propiedad: Propiedad):
        propiedad_dto = self.fabrica_vuelos.crear_objeto(propiedad, MapeadorReserva())
        db.session.add(propiedad_dto)

    def actualizar(self, propiedad: Propiedad):
        # TODO
        raise NotImplementedError

    def eliminar(self, propiedad_id: UUID):
        # TODO
        raise NotImplementedError