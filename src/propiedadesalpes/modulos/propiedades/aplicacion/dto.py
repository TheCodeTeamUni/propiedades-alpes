from dataclasses import dataclass, field
from propiedadesalpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class PropiedadDTO(DTO):
    eventId: str = field(default_factory=str)
    fecha_creacion: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    descripcion: str = field(default_factory=str)
    tipo: str = field(default_factory=str)
    piso: str = field(default_factory=str)
    longitud: str = field(default_factory=str)
    latitud: str = field(default_factory=str)