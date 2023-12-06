import json
from database import mensajes, problema, creyentes
from schemas import MensajesRequestModel, MensajesResponseModel

def crear_mensaje(request: MensajesRequestModel):
    mensaje = mensajes.create(
        mensaje=request.mensaje,
        id_problema=request.id_problema,
        activo=request.activo,
    )
    return mensaje

def buscar_mensajes():
    request = mensajes.select().where(mensajes.activo == 1)
    resultados = []
    for fila in request:
        modelo = {
            'id': fila.id,
            'mensaje': fila.mensaje,
            'fecha': fila.fecha.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'id_problema': fila.id_problema.id,
            'activo': fila.activo
        }
        resultados.append(modelo)
    json_result = json.dumps({'Mensajes': resultados})
    data = json.loads(json_result)
    return data

def eliminar_mensaje(id):
    datos = mensajes.select().where(mensajes.id == id).first()
    if datos:
        setattr(datos, 'activo', 0)
        datos.save()
        return 'exito'
    return 'error'


def buscar_conversacion(id_problema):
    problema = problema.select().join(creyentes).where(problema.id == id_problema, problema.activo == 1).first()

    if problema:
        modelo_problema = {
            'id': problema.id,
            'id_creyente': problema.id_creyente.id,
            'nombre_creyente': problema.id_creyente.nombre,
            'nombre_problema': problema.nombre_problema,
            'descripcion': problema.descripcion,
            'fecha_creacion': problema.fecha_creacion.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'revision': problema.revision.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'id_estado': problema.id_estado.id,
            'activo': problema.activo
        }

        mensajes = mensajes.select().where((mensajes.activo == 1) & (mensajes.id_problema == id_problema))
        lista_mensajes = []
        for mensaje in mensajes:
            modelo_mensaje = {
                'id': mensaje.id,
                'mensaje': mensaje.mensaje,
                'fecha': mensaje.fecha.strftime('%Y-%m-%dT%H:%M:%SZ'),
                'id_problema': mensaje.id_problema.id,
                'activo': mensaje.activo
            }
            lista_mensajes.append(modelo_mensaje)

        conversacion = {
            'problema': modelo_problema,
            'mensajes': lista_mensajes
        }

        {'conversacion': [conversacion]}
        resul = json.dumps(conversacion)
        data = json.loads(resul)
        return data
    else:
        return json.dumps({'conversacion': []})


