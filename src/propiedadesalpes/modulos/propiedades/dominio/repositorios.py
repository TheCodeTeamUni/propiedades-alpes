from abc import ABC
from propiedadesalpes.seedwork.dominio.repositorios import Repositorio

class RepositorioPropiedades(Repositorio, ABC):
    ...

class RepositorioProveedores(Repositorio, ABC):
    ...