from propiedadesalpes.modulos.propiedades.dominio.eventos import PropiedadCreada
from propiedadesalpes.seedwork.aplicacion.handlers import Handler
from propiedadesalpes.modulos.propiedades.infraestructura.despachadores import Despachador

class HandlerReservaIntegracion(Handler):

    @staticmethod
    def handle_propiedad_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedad')

    @staticmethod
    def handle_propiedad_cancelada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedad')

    @staticmethod
    def handle_propiedad_aprobada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedad')

    @staticmethod
    def handle_propiedad_pagada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedad')


    