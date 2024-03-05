from propiedadesalpes.config.db import db
from propiedadesalpes.modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from propiedadesalpes.modulos.propiedades.dominio.objetos_valor import NombrePropiedades, Odo, Leg, Segmento, Itinerario, CodigoIATA
from propiedadesalpes.modulos.propiedades.dominio.entidades import Proveedor, Propiedadespuerto, Propiedad
from propiedadesalpes.modulos.propiedades.dominio.fabricas import FabricaPropiedades
from .dto import Reserva as ReservaDTO
from .mapeadores import MapeadorReserva
from uuid import UUID

class RepositorioPropiedadesSQLite(RepositorioPropiedades):

    def __init__(self):
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades

    def obtener_por_id(self, id: UUID) -> Propiedad:
        propiedad_dto = db.session.query(ReservaDTO).filter_by(id=str(id)).one()
        return self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorReserva())

    def obtener_todos(self) -> list[Propiedad]:
        # TODO
        raise NotImplementedError

    def agregar(self, propiedad: Propiedad):
        propiedad_dto = self.fabrica_propiedades.crear_objeto(propiedad, MapeadorReserva())
        db.session.add(propiedad_dto)

    def actualizar(self, propiedad: Propiedad):
        # TODO
        raise NotImplementedError

    def eliminar(self, propiedad_id: UUID):
        # TODO
        raise NotImplementedError