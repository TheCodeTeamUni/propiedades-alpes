from pulsar.schema import *
from propiedadesalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class ReservaCreadaPayload(Record):
    id_propiedad = String()
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()

class EventoReservaCreada(EventoIntegracion):
    data = ReservaCreadaPayload()