from propiedadesalpes.seedwork.aplicacion.comandos import Comando
from propiedadesalpes.modulos.propiedades.aplicacion.dto import ReservaDTO
from .base import CrearPropiedadBaseHandler
from dataclasses import dataclass, field
from propiedadesalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from propiedadesalpes.modulos.propiedades.dominio.entidades import Propiedad
from propiedadesalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from propiedadesalpes.modulos.propiedades.aplicacion.mapeadores import MapeadorReserva
from propiedadesalpes.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades

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
        propiedad_dto = ReservaDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   itinerarios=comando.itinerarios)

        propiedad: Propiedad = self.fabrica_vuelos.crear_objeto(propiedad_dto, MapeadorReserva())
        propiedad.crear_propiedad(propiedad)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearPropiedad)
def ejecutar_comando_crear_propiedad(comando: CrearPropiedad):
    handler = CrearPropiedadHandler()
    handler.handle(comando)
    