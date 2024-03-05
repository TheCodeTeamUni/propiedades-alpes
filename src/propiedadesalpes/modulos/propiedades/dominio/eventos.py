from __future__ import annotations
from dataclasses import dataclass, field
from propiedadesalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
import uuid

class EventoPropiedad(EventoDominio):
    ...
@dataclass
class PropiedadCreada(EventoPropiedad):
    id_propiedad = str = None
    fecha_creacion: str = None
    nombre: str = None
    descripcion: str = None
    tipo: str = None
    piso: str = None
    longitud: str = None
    latitud: str = None