import propiedadesalpes.seedwork.presentacion.api as api
import json
from propiedadesalpes.modulos.propiedades.aplicacion.servicios import ServicioPropiedad
from propiedadesalpes.modulos.propiedades.aplicacion.dto import ReservaDTO
from propiedadesalpes.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from propiedadesalpes.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from propiedadesalpes.modulos.propiedades.aplicacion.comandos.crear_propiedad import CrearPropiedad
from propiedadesalpes.modulos.propiedades.aplicacion.queries.obtener_propiedad import ObtenerReserva
from propiedadesalpes.seedwork.aplicacion.comandos import ejecutar_commando
from propiedadesalpes.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('propiedades', '/propiedades')


@bp.route('/propiedad', methods=('POST',))
def crear_propiedad():
    try:
        propiedad_dict = request.json

        map_propiedad = MapeadorPropiedadDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)

        comando = CrearPropiedad(propiedad_dto.eventId, propiedad_dto.fecha_creacion, propiedad_dto.nombre,
                                 propiedad_dto.descripcion, propiedad_dto.tipo, propiedad_dto.piso, propiedad_dto.longitud, propiedad_dto.latitud)

        ejecutar_commando(comando)

        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')


@bp.route('/propiedad', methods=('GET',))
@bp.route('/propiedad/<id>', methods=('GET',))
def dar_propiedad_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerReserva(id))
        map_propiedad = MapeadorPropiedadDTOJson()

        return map_propiedad.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]
