from propiedadesalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from propiedadesalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from propiedadesalpes.modulos.propiedades.dominio.entidades import Propiedad
from propiedadesalpes.modulos.propiedades.dominio.objetos_valor import Itinerario, Odo, Segmento, Leg
from .dto import PropiedadDTO

from datetime import datetime


class MapeadorPropiedadDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        print("MapeadorPropiedadDTOJson EventId: ", externo.get('eventId'))
        print("\n")

        event_id = externo.get('eventId')
        fecha_creacion = externo.get('fecha_creacion')
        nombre = externo.get('nombre')
        descripcion = externo.get('descripcion')
        tipo = externo.get('tipo')
        piso = externo.get('piso')
        longitud = externo.get('longitud')
        latitud = externo.get('latitud')

        propiedad_dto = PropiedadDTO(eventId=event_id, fecha_creacion=fecha_creacion, nombre=nombre,
                                     descripcion=descripcion, tipo=tipo, piso=piso, longitud=longitud, latitud=latitud)

        print("MapeadorPropiedadDTOJson EXTERNO TO DTO: ", propiedad_dto)
        print("\n")

        return propiedad_dto

    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__


class MapeadorPropiedad(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:

        _id = str(entidad.id)
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        nombre = entidad.nombre
        descripcion = entidad.descripcion
        tipo = entidad.tipo
        piso = entidad.piso
        longitud = entidad.longitud
        latitud = entidad.latitud

        return PropiedadDTO(_id, fecha_creacion, nombre, descripcion, tipo, piso, longitud, latitud)

    
    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad(
            id=dto.eventId,
            fecha_creacion=datetime.strptime(dto.fecha_creacion, self._FORMATO_FECHA),
            nombre=dto.nombre,
            descripcion=dto.descripcion,
            tipo=dto.tipo,
            piso=dto.piso,
            longitud=dto.longitud,
            latitud=dto.latitud
        )

        return propiedad
