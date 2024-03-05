from pulsar.schema import *
from .utils import time_millis
import uuid

'''class LocalizaciónAsignada(Record):
    id = String(),
    id_correlacion = String(),
    propiedad_id = String()
    latitud = Double()
    longitud = Double()
    fecha_creacion = Long()
 
class LocalizacioRevertida(Record):
    id = String()
    id_correlacion = String()
    propiedad_id = String()
    fecha_actualizacion = Long()

class EventoLocalizacion(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="EventoLocalizacion")
    datacontenttype = String()
    service_name = String(default="propiedades.localizacion")
    propiedad_localizada = PropiedadLocalizada
    localizacion_revertida = LocalizacionRevertida

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)'''
