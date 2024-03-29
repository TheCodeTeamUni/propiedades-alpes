from __future__ import annotations
from dataclasses import dataclass, field

import propiedadesalpes.modulos.propiedades.dominio.objetos_valor as ov
from propiedadesalpes.modulos.propiedades.dominio.eventos import PropiedadCreada
from propiedadesalpes.seedwork.dominio.entidades import AgregacionRaiz


@dataclass
class Propiedad(AgregacionRaiz):
    id: str = None
    fecha_creacion: str = None
    nombre: str = None
    descripcion: str = None
    tipo: str = None
    piso: str = None
    longitud: str = None
    latitud: str = None

    def crear_propiedad(self, propiedad: Propiedad):
        self.id = propiedad.id
        self.fecha_creacion = propiedad.fecha_creacion
        self.nombre = propiedad.nombre
        self.descripcion = propiedad.descripcion
        self.tipo = propiedad.tipo
        self.piso = propiedad.piso
        self.longitud = propiedad.longitud
        self.latitud = propiedad.latitud

        self.agregar_evento(PropiedadCreada(fecha_creacion=self.fecha_creacion, nombre=self.nombre,
                            descripcion=self.descripcion, tipo=self.tipo, piso=self.piso, longitud=self.longitud, latitud=self.latitud))
