import aeroalpes.seedwork.presentacion.api as api
import json
from aeroalpes.modulos.vuelos.aplicacion.servicios import ServicioReserva
from aeroalpes.modulos.vuelos.aplicacion.dto import ReservaDTO
from aeroalpes.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from aeroalpes.modulos.vuelos.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from aeroalpes.modulos.vuelos.aplicacion.comandos.crear_reserva import CrearPropiedad
from aeroalpes.modulos.vuelos.aplicacion.queries.obtener_reserva import ObtenerReserva
from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando
from aeroalpes.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('propiedades', '/propiedades')

@bp.route('/propiedad', methods=('POST',))
def crear_propiedad():
    try:
        propiedad_dict = request.json

        map_propiedad = MapeadorPropiedadDTOJson()
        reserva_dto = map_propiedad.externo_a_dto(propiedad_dict)

        comando = CrearPropiedad(reserva_dto.fecha_creacion, reserva_dto.fecha_actualizacion, reserva_dto.id, reserva_dto.itinerarios)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/reserva', methods=('GET',))
@bp.route('/reserva/<id>', methods=('GET',))
def dar_reserva(id=None):
    if id:
        sr = ServicioReserva()
        map_reserva = MapeadorPropiedadDTOJson()
        
        return map_reserva.dto_a_externo(sr.obtener_reserva_por_id(id))
    else:
        return [{'message': 'GET!'}]

@bp.route('/reserva-query', methods=('GET',))
@bp.route('/reserva-query/<id>', methods=('GET',))
def dar_reserva_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerReserva(id))
        map_reserva = MapeadorPropiedadDTOJson()
        
        return map_reserva.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]