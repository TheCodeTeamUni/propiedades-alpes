from propiedadesalpes.seedwork.aplicacion.servicios import Servicio
from propiedadesalpes.modulos.propiedades.dominio.entidades import Propiedad
from propiedadesalpes.modulos.propiedades.dominio.fabricas import FabricaPropiedades
from propiedadesalpes.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from propiedadesalpes.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades
from propiedadesalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .mapeadores import MapeadorPropiedad

from .dto import ReservaDTO

import asyncio

class ServicioPropiedad(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_vuelos: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos       
    
    def crear_propiedad(self, propiedad_dto: ReservaDTO) -> ReservaDTO:
        propiedad: Propiedad = self.fabrica_vuelos.crear_objeto(propiedad_dto, MapeadorPropiedad())
        propiedad.crear_propiedad(propiedad)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        return self.fabrica_vuelos.crear_objeto(propiedad, MapeadorPropiedad())

    def obtener_propiedad_por_id(self, id) -> ReservaDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        return self.fabrica_vuelos.crear_objeto(repositorio.obtener_por_id(id), MapeadorPropiedad())

