from __future__ import annotations
from dataclasses import dataclass, field
from aeroalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
import uuid

@dataclass
class PropiedadCreada(EventoDominio):
    id_propiedad = uuid.UUID = None
    fecha_creacion: str = None
    nombre: str = None
    descripcion: str = None
    tipo: str = None
    piso: str = None
    longitud: str = None
    latitud: str = None