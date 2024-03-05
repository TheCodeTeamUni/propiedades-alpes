from pulsar.schema import *
from .utils import time_millis
import uuid


class AgregarPlano(Record):
    id_propiedad = String(),
    dimensiones = String(),
    descripcion = String(),
    plano = String(),
    
 

class ComandoAgregarPlano(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="AgregarPlano")
    datacontenttype = String()
    service_name = String(default="planos.propiedadesalpes")
    data = AgregarPlano

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)