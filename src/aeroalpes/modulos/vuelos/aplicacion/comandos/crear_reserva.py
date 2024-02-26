from aeroalpes.seedwork.aplicacion.comandos import Comando
from aeroalpes.modulos.vuelos.aplicacion.dto import ReservaDTO
from .base import CrearPropiedadBaseHandler
from dataclasses import dataclass, field
from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from aeroalpes.modulos.vuelos.dominio.entidades import Propiedad
from aeroalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from aeroalpes.modulos.vuelos.aplicacion.mapeadores import MapeadorReserva
from aeroalpes.modulos.vuelos.infraestructura.repositorios import RepositorioPropiedades

@dataclass
class CrearPropiedad(Comando):
    eventId: int
    fecha_creacion: str
    nombre: str
    descripcion: str
    tipo: str
    piso: str
    longitud: str
    latitud: str
    
class CrearPropiedadHandler(CrearPropiedadBaseHandler):
    
    def handle(self, comando: CrearPropiedad):
        reserva_dto = ReservaDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   itinerarios=comando.itinerarios)

        reserva: Propiedad = self.fabrica_vuelos.crear_objeto(reserva_dto, MapeadorReserva())
        reserva.crear_reserva(reserva)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, reserva)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearPropiedad)
def ejecutar_comando_crear_propiedad(comando: CrearPropiedad):
    handler = CrearPropiedadHandler()
    handler.handle(comando)
    