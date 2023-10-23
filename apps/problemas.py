import json
from database import Problema, Creyentes
from schemas import ProblemaRequestModel, ProblemaResponseModel


def crear_problema(request: ProblemaRequestModel):
    request = Problema.create(
        id_creyente=request.id_creyente,
        descripcion=request.descripcion,
        fecha_creacion=request.fecha_creacion,
        revision=request.revision,
        id_estado=request.id_estado,
        activo=request.activo,
    )
    return request


def buscar_problemas():
    request = Problema.select().where(Problema.activo == 1).order_by(Problema.revision.asc())
    resultados = []

    for fila in request:
        creyente = Creyentes.get(Creyentes.id == fila.id_creyente.id)
        modelo = {
            'id': fila.id,
            'id_creyente': fila.id_creyente.id,
            'nombre_creyente': creyente.nombre,
            'descripcion': fila.descripcion,
            'fecha_creacion': fila.fecha_creacion.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'revision': fila.revision.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'id_estado': fila.id_estado.id,
            'activo': fila.activo
        }
        resultados.append(modelo)

    json_result = json.dumps({'Problemas': resultados})
    data = json.loads(json_result)

    return data



def buscar_creyente():
    pass


def cambiar_creyentes():
    pass


def elimnar_problema(jid):
    datos = Problema.select().where(Problema.id == jid).first()
    if datos:
        setattr(datos, 'activo', 0)
        datos.save()
        return 'exito'
    return 'error'

def main_menu(gpo):
    problema = Problema.select().join(Creyentes).where(
        ((Creyentes.id_grupo == gpo) & (Problema.activo == 1)) | ((Creyentes.id_grupo == 3) & (Problema.activo == 1))
    ).order_by(Problema.revision.asc())

    resultados = []

    for fila in problema:
        creyente = Creyentes.get(Creyentes.id == fila.id_creyente.id)
        modelo = {
            'id': fila.id,
            'id_creyente': fila.id_creyente.id,
            'nombre_creyente': creyente.nombre,
            'descripcion': fila.descripcion,
            'fecha_creacion': fila.fecha_creacion.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'revision': fila.revision.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'id_estado': fila.id_estado.id,
            'activo': fila.activo
        }
        resultados.append(modelo)

    json_result = json.dumps({'Problemas': resultados})
    data = json.loads(json_result)
    return data