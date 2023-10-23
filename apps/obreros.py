import json
from database import Obreros
from schemas import ObrerosRequestModel


def crear_obrero(request: ObrerosRequestModel):
    request = Obreros.create(
        nombre=request.nombre,
        telefono=request.telefono,
        direccion=request.direccion,
        id_grupo=request.id_grupo,
        activo=request.activo,
        usuario=request.usuario,
        contrasena=request.contrasena
    )
    return request


def buscar_obreros():
    request = Obreros.select().where(Obreros.activo == 1)
    resultados = []
    for fila in request:
        modelo = {
            'id': fila.id,
            'nombre': fila.nombre,
            'telefono': fila.telefono,
            'direccion': fila.direccion,
            'id_grupo': fila.id_grupo.id,
            'activo': fila.activo,
            'usuario': fila.usuario,
            'contrasena': fila.contrasena
        }
        resultados.append(modelo)
    json_result = json.dumps({'Obreros': resultados})
    data = json.loads(json_result)
    return data


def buscar_obrero():
    pass


def cambiar_obrero():
    pass


def elimnar_obrero(jid):
    datos = Obreros.select().where(Obreros.id == jid).first()
    if datos:
        setattr(datos, 'activo', 0)
        datos.save()
        return 'exito'
    return 'error'
