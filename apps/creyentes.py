import json
from database import Creyentes
from schemas import CreyentesRequestModel, CreyentesResponseModel


def crear_creyentes(request: CreyentesRequestModel):
    request = Creyentes.create(
        nombre=request.nombre,
        telefono=request.telefono,
        direccion=request.direccion,
        dias_disp=request.direccion,
        id_grupo=request.id_grupo,
        activo=request.activo,
    )
    return request


def buscar_creyentes():
    request = Creyentes.select().where(Creyentes.activo == 1)
    resultados = []
    for fila in request:
        modelo = {
            'id': fila.id,
            'nombre': fila.nombre,
            'telefono': fila.telefono,
            'direccion': fila.direccion,
            'dias_disp': fila.direccion,
            'id_grupo': fila.id_grupo.id,
            'activo': fila.activo
        }
        resultados.append(modelo)
    json_result = json.dumps({'Creyentes': resultados})
    data = json.loads(json_result)
    return data


def buscar_creyente():
    pass


def cambiar_creyentes():
    pass


def elimnar_creyentes(jid):
    datos = Creyentes.select().where(Creyentes.id == jid).first()
    if datos:
        setattr(datos, 'activo', 0)
        datos.save()
        return 'exito'
    return 'error'
