# Propiedade de los alpes - The Code Team

## Estructura del proyecto

La estructra del proyecto es la siguiente:

- **api**: En este módulo se modificó el API de `propiedad.py` el cual cuenta con los endpoints: `/propiedad` y `/propiedad/<id>`, los cuales por detrás de escenas usan un patrón CQRS como la base de su comunicación.
- **modulos/../aplicacion**: Este módulo ahora considera los sub-módulos: `queries` y `comandos`. En dichos directorios podrá ver como se desacopló las diferentes operaciones lectura y escritura.
- **modulos/../aplicacion/handlers.py**: Estos son los handlers de aplicación que se encargan de oir y reaccionar a eventos. Si consulta el módulo de clientes podra ver que tenemos handlers para oir y reaccionar a los eventos de dominio para poder continuar con una transacción.
- **modulos/../dominio/eventos.py**: Este archivo contiene todos los eventos de dominio que son disparados cuando una actividad de dominio es ejecutada de forma correcta.
- **modulos/../infraestructura/consumidores.py**: Este archivo cuenta con toda la lógica en términos de infrastructura para consumir los eventos y comandos que provienen del broker de eventos.
- **modulos/../infraestructura/despachadores.py**: Este archivo cuenta con toda la lógica en terminos de infrastructura para publicar los eventos y comandos de integración en el broker de eventos.
- **modulos/../infraestructura/schema**: En este directorio encontramos la definición de los eventos y comandos de integración.
- **seedwork/aplicacion/comandos.py**: Definición general de los comandos, handlers e interface del despachador.
- **seedwork/aplicacion/queries.py**: Definición general de los queries, handlers e interface del despachador.
- **seedwork/infraestructura/uow.py**: La Unidad de Trabajo (UoW) mantiene una lista de objetos afectados por una transacción de negocio y coordina los cambios de escritura.

## PropiedadesAlpes

### Ejecutar base de datos

Desde el directorio principal ejecute el siguiente comando.

```bash
docker-compose --profile db up
```

### Ejecutar Pulsar

Desde el directorio principal ejecute el siguiente comando.

```bash
docker-compose --profile pulsar up
```

### Ejecutar Aplicación Propiedades

Desde el directorio principal ejecute el siguiente comando.

```bash
flask --app src/propiedadesalpes/api run
```

Siempre puede ejecutarlo en modo DEBUG:

```bash
flask --app src/propiedadesalpes/api --debug run
```

### Ejecutar Aplicación Contratos

Debe tener creado un entorno virtual e instalado las dependecias. Desde el directorio src ejecute el siguiente comando:

```bash
uvicorn contratos.main:app --host localhost --port 8001 --reload
```

### Ejecutar Aplicación Localización

Debe tener creado un entorno virtual e instalado las dependecias. Desde el directorio src ejecute el siguiente comando:

```bash
uvicorn localizacion.main:app --host localhost --port 8002 --reload
```

### Ejecutar Aplicación Planos

Debe tener creado un entorno virtual e instalado las dependecias. Desde el directorio src ejecute el siguiente comando:

```bash
uvicorn planos.main:app --host localhost --port 8003 --reload
```

### Ejecutar Aplicación Compañias

Debe tener creado un entorno virtual e instalado las dependecias. Desde el directorio src ejecute el siguiente comando:

```bash
uvicorn companias.main:app --host localhost --port 8004 --reload
```

### Ejecutar el BFF

Debe tener creado un entorno virtual e instalado las dependecias. Desde el directorio src ejecute el siguiente comando:

```bash
uvicorn bff_web.main:app --host localhost --port 9000 --reload
```

Para ingresar a la interza gráfica de GraphQL, debe ir al navegador:
```bash
http:localhost:9000/v1
```


## Comandos útiles

### Listar contenedoras en ejecución

```bash
docker ps
```

### Listar todas las contenedoras

```bash
docker ps -a
```

### Parar contenedora

```bash
docker stop <id_contenedora>
```

### Eliminar contenedora

```bash
docker rm <id_contenedora>
```

### Listar imágenes

```bash
docker images
```

### Eliminar imágenes

```bash
docker images rm <id_imagen>
```

### Acceder a una contendora

```bash
docker exec -it <id_contenedora> sh
```

### Kill proceso que esta usando un puerto

```bash
fuser -k <puerto>/tcp
```

### Correr docker-compose usando profiles

```bash
docker-compose --profile <pulsar|propiedadesalpes|ui|notificacion> up
```
