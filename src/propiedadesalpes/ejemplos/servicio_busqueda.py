from propiedadesalpes.modulos.propiedades.dominio.objetos_valor import Odo, ParametroBusca, Segmento, Leg, CodigoIATA, Itinerario
from propiedadesalpes.modulos.propiedades.dominio.entidades import Proveedor,Propiedadespuerto

def filtrar_mejores_itinerarios(itinerarios: list[Itinerario]) -> list[Itinerario]:
    # Logica compleja para filtrar itinerarios
    ...
    return itinerarios


def buscar_itinerarios(odos: list[Odo], parametros: ParametroBusca) -> list[Itinerario]:
    itinerarios: list[Itinerario] = list()
    proveedores: list[Proveedor] = rp.obtener_todos()

    itinerarios.append([proveedor.obtener_itinerarios(odos, parametros) for proveedor in proveedores])

    return filtrar_mejores_itinerarios(itinerarios)

# origen=Propiedadespuerto(codigo=CodigoIATA(codigo="CPT"), nombre="Cape Town International")
# destino=Propiedadespuerto(codigo=CodigoIATA(codigo="JFK"), nombre="JFK International Airport")
# legs=[Leg(origen=origen, destino=destino)]
# segmentos = [Segmento(legs)]
# ruta = Odo(segmentos=segmentos)
# itinerarios = buscar_itinerarios(ruta, ParametroBusca(pasajeros=list()))
# print(itinerarios)