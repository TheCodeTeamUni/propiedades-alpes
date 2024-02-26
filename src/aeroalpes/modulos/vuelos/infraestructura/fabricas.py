from dataclasses import dataclass, field
from aeroalpes.seedwork.dominio.fabricas import Fabrica
from aeroalpes.seedwork.dominio.repositorios import Repositorio
from aeroalpes.modulos.vuelos.dominio.repositorios import RepositorioProveedores, RepositorioPropiedades
from .repositorios import RepositorioPropiedadesSQLite, RepositorioProveedoresSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropiedades.__class__:
            return RepositorioPropiedadesSQLite()
        else:
            raise ExcepcionFabrica()