from pulsar.schema import *
from .utils import time_millis
import uuid


class AgregarUbicacion(Record):
    id_propiedad = String(),
    latitud = Double()
    longitud = Double()
    
 

class ComandoAgregarUbicacion(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="AgregarUbicacion")
    datacontenttype = String()
    service_name = String(default="ubicacion.propiedadesalpes")
    data = AgregarUbicacion

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)