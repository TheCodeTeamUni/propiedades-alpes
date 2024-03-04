from pulsar.schema import *
from .utils import time_millis
import uuid

class AgregarCompania(Record):
    id_compania = String()
    nombre = String()
    telefono = String()
    direccion_ppal = String()

class ComandoAgregarCompania(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="AgregarCompania")
    datacontenttype = String()
    service_name = String(default="companias.propiedadesalpes")
    data = AgregarCompania

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)