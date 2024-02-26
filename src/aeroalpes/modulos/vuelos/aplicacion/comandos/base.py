from aeroalpes.seedwork.aplicacion.comandos import ComandoHandler
from aeroalpes.modulos.vuelos.infraestructura.fabricas import FabricaRepositorio
from aeroalpes.modulos.vuelos.dominio.fabricas import FabricaPropiedades

class CrearPropiedadBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_vuelos: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos    
    