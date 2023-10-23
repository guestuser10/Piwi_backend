import json

from database import *
from schemas import *


def crear_grupo(request: GruposRequestModel):
    request = Grupos.create(
            nombre=request.nombre,
            activo=request.activo
        )
    return request


def buscar_grupos():
    request = Grupos.select().where(Grupos.activo == '1')
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
    datos = Grupos.select().where(Grupos.id == jid).first()
    if datos:
        setattr(datos, 'activo', 0)
        datos.save()
        return 'exito'
    return 'error'

