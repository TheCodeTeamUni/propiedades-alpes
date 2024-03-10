from propiedadesalpes.seedwork.aplicacion.comandos import Comando
from propiedadesalpes.modulos.propiedades.aplicacion.dto import PropiedadDTO
from .base import CrearPropiedadBaseHandler
from dataclasses import dataclass, field
from propiedadesalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from propiedadesalpes.modulos.propiedades.dominio.entidades import Propiedad
from propiedadesalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from propiedadesalpes.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
from propiedadesalpes.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades


@dataclass
class CrearPropiedad(Comando):
    eventId: str
    fecha_creacion: str
    nombre: str
    descripcion: str
    tipo: str
    piso: str
    longitud: str
    latitud: str


class CrearPropiedadHandler(CrearPropiedadBaseHandler):

    def handle(self, comando: CrearPropiedad):
        propiedad_dto = PropiedadDTO(eventId=comando.eventId, fecha_creacion=comando.fecha_creacion, nombre=comando.nombre,
                                     descripcion=comando.descripcion, tipo=comando.tipo, piso=comando.piso, longitud=comando.longitud, latitud=comando.latitud)

        propiedad: Propiedad = self.fabrica_propiedades.crear_objeto(
            propiedad_dto, MapeadorPropiedad())
        propiedad.crear_propiedad(propiedad)

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioPropiedades)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearPropiedad)
def ejecutar_comando_crear_propiedad(comando: CrearPropiedad):
    handler = CrearPropiedadHandler()
    handler.handle(comando)
