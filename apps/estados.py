import json

from database import Estados
from schemas import EstadosRequestModel, EstadosResponseModel


model = Estados


def crear_estado(request: EstadosRequestModel):
    request = model.create(
            nombre=request.nombre,
            activo=request.activo
        )
    return request


def buscar_estados():
    request = model.select().where(model.activo == '1')
    resultados = []
    for fila in request:
        modelo = {'id': fila.id, 'nombre': fila.nombre, 'activo': fila.activo}
        resultados.append(modelo)
    json_result = json.dumps({'Estados': resultados})
    data = json.loads(json_result)
    return data


def buscar_estado():
    pass


def cambiar_estado():
    pass


def elimnar_estado(jid):
    datos = model.select().where(model.id == jid).first()
    if datos:
        setattr(datos, 'activo', 0)
        datos.save()
        return 'exito'
    return 'error'
