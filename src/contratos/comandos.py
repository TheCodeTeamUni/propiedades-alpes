from pulsar.schema import *
from .utils import time_millis
import uuid

class AgregarContrato(Record):
    id_propiedad = String()
    monto = Float()
    comprador = String()
    vendedor = String()
    inquilino = String()
    arrendador = String()

class ComandoAgregarContrato(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="AgregarContrato")
    datacontenttype = String()
    service_name = String(default="contratos.aeroalpes")
    data = AgregarContrato

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
