import json

from database import *
from schemas import *


def crear_grupo(request: GruposRequestModel):
    request = grupos.create(
            nombre=request.nombre,
            activo=request.activo
        )
    return request


def buscar_grupos():
    request = grupos.select().where(grupos.activo == '1')
    resultados = []
    for fila in request:
        grupo = GruposResponseModel(id=fila.id, nombre=fila.nombre, activo=fila.activo)
        modelo = {'id': grupo.id, 'nombre': grupo.nombre, 'activo': grupo.activo}
        resultados.append(modelo)
    json_result = json.dumps({'Grupos': resultados})  # Envolver en un diccionario con la clave 'Grupos'
    data = json.loads(json_result)
    return data


def buscar_grupo():
    pass


def cambiar_grupo():
    pass


def elimnar_grupo(jid):
    datos = grupos.select().where(grupos.id == jid).first()
    if datos:
        setattr(datos, 'activo', 0)
        datos.save()
        return 'exito'
    return 'error'

