import json
from database import Creyentes
from schemas import CreyentesRequestModel, CreyentesResponseModel


def crear_creyentes(request: CreyentesRequestModel):
    request = Creyentes.create(
        nombre=request.nombre,
        telefono=request.telefono,
        direccion=request.direccion,
        dias_disp=request.dias_disp,
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
            'dias_disp': fila.dias_disp,
            'id_grupo': fila.id_grupo.id,
            'activo': fila.activo
        }
        resultados.append(modelo)
    json_result = json.dumps({'Creyentes': resultados})
    data = json.loads(json_result)
    return data


def buscar_creyente_por_id(id_creyente):
    try:
        creyente = Creyentes.get((Creyentes.id == id_creyente) & (Creyentes.activo == 1))
        resultado = {
            'id': creyente.id,
            'nombre': creyente.nombre,
            'telefono': creyente.telefono,
            'direccion': creyente.direccion,
            'dias_disp': creyente.dias_disp,
            'id_grupo': creyente.id_grupo.id,
            'activo': creyente.activo
        }
        return {'Creyente': resultado}
    except Creyentes.DoesNotExist:
        return {'error': 'Creyente no encontrado'}


def cambiar_creyentes():
    pass


def elimnar_creyentes(jid):
    datos = Creyentes.select().where(Creyentes.id == jid).first()
    if datos:
        setattr(datos, 'activo', 0)
        datos.save()
        return 'exito'
    return 'error'


def barra_busqueda_miembros(search_text):
    request = Creyentes.select().where(Creyentes.activo == 1 & Creyentes.nombre.contains(search_text))
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
