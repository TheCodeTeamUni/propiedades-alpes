from propiedadesalpes.seedwork.dominio.repositorios import Mapeador
from propiedadesalpes.modulos.propiedades.dominio.objetos_valor import NombrePropiedades, Odo, Leg, Segmento, Itinerario, CodigoIATA
from propiedadesalpes.modulos.propiedades.dominio.entidades import Propiedad
from .dto import Propiedad as PropiedadDTO


class MapeadorPropiedad(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:

        propiedad_dto = PropiedadDTO(entidad.id, entidad.fecha_creacion.strftime(
            self._FORMATO_FECHA), entidad.nombre, entidad.descripcion, entidad.tipo, entidad.piso, entidad.longitud, entidad.latitud)

        return propiedad_dto

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad(dto.id, dto.fecha_creacion, dto.nombre,
                              dto.descripcion, dto.tipo, dto.piso, dto.longitud, dto.latitud)

        return propiedad
