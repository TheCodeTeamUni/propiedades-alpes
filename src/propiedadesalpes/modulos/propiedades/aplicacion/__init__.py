from pydispatch import dispatcher
from .handlers import HandlerPropiedadIntegracion
from propiedadesalpes.modulos.propiedades.dominio.eventos import PropiedadCreada

dispatcher.connect(HandlerPropiedadIntegracion.handle_propiedad_creada, signal=f'{PropiedadCreada.__name__}Integracion')