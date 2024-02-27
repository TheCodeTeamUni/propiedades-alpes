from pydispatch import dispatcher

from .handlers import HandlerReservaIntegracion

from propiedadesalpes.modulos.propiedades.dominio.eventos import PropiedadCreada, ReservaCancelada, ReservaAprobada, ReservaPagada

dispatcher.connect(HandlerReservaIntegracion.handle_propiedad_creada, signal=f'{PropiedadCreada.__name__}Integracion')
dispatcher.connect(HandlerReservaIntegracion.handle_propiedad_cancelada, signal=f'{ReservaCancelada.__name__}Integracion')
dispatcher.connect(HandlerReservaIntegracion.handle_propiedad_pagada, signal=f'{ReservaPagada.__name__}Integracion')
dispatcher.connect(HandlerReservaIntegracion.handle_propiedad_aprobada, signal=f'{ReservaAprobada.__name__}Integracion')