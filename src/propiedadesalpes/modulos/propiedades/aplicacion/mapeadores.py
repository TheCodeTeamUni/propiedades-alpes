from propiedadesalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from propiedadesalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from propiedadesalpes.modulos.propiedades.dominio.entidades import Propiedad, Aeropuerto
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

"""
class MapeadorReserva(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_itinerario(self, itinerario_dto: ItinerarioDTO) -> Itinerario:
        odos = list()

        for odo_dto in itinerario_dto.odos:
            segmentos = list()
            for seg_dto in odo_dto.segmentos:

                legs = list()

                for leg_dto in seg_dto.legs:
                    destino = Aeropuerto(codigo=leg_dto.destino.get(
                        'codigo'), nombre=leg_dto.destino.get('nombre'))
                    origen = Aeropuerto(codigo=leg_dto.origen.get(
                        'codigo'), nombre=leg_dto.origen.get('nombre'))
                    fecha_salida = datetime.strptime(
                        leg_dto.fecha_salida, self._FORMATO_FECHA)
                    fecha_llegada = datetime.strptime(
                        leg_dto.fecha_llegada, self._FORMATO_FECHA)

                    leg: Leg = Leg(fecha_salida, fecha_llegada,
                                   origen, destino)

                    legs.append(leg)

                segmentos.append(Segmento(legs))

            odos.append(Odo(segmentos))

        return Itinerario(odos)

    def obtener_tipo(self) -> type:
        return Reserva.__class__

    def locacion_a_dict(self, locacion):
        if not locacion:
            return dict(codigo=None, nombre=None, fecha_actualizacion=None, fecha_creacion=None)

        return dict(
            codigo=locacion.codigo,   nombre=locacion.nombre,   fecha_actualizacion=locacion.fecha_actualizacion.strftime(self._FORMATO_FECHA),   fecha_creacion=locacion.fecha_creacion.strftime(self._FORMATO_FECHA)
        )

    def entidad_a_dto(self, entidad: Reserva) -> ReservaDTO:

        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(
            self._FORMATO_FECHA)
        _id = str(entidad.id)
        itinerarios = list()

        for itin in entidad.itinerarios:
            odos = list()
            for odo in itin.odos:
                segmentos = list()
                for seg in odo.segmentos:
                    legs = list()
                    for leg in seg.legs:
                        fecha_salida = leg.fecha_salida.strftime(
                            self._FORMATO_FECHA)
                        fecha_llegada = leg.fecha_llegada.strftime(
                            self._FORMATO_FECHA)
                        origen = self.locacion_a_dict(leg.origen)
                        destino = self.locacion_a_dict(leg.destino)
                        leg = LegDTO(
                            fecha_salida=fecha_salida, fecha_llegada=fecha_llegada, origen=origen, destino=destino)

                        legs.append(leg)

                    segmentos.append(SegmentoDTO(legs))
                odos.append(OdoDTO(segmentos))
            itinerarios.append(ItinerarioDTO(odos))

        return ReservaDTO(fecha_creacion, fecha_actualizacion, _id, itinerarios)

    def dto_a_entidad(self, dto: ReservaDTO) -> Reserva:
        propiedad = Reserva()
        propiedad.itinerarios = list()

        itinerarios_dto: list[ItinerarioDTO] = dto.itinerarios

        for itin in itinerarios_dto:
            propiedad.itinerarios.append(self._procesar_itinerario(itin))

        return propiedad
"""