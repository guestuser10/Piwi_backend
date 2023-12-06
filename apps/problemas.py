import json
from database import Problema, Creyentes, Estados
from schemas import ProblemaRequestModel, ProblemaResponseModel


def crear_problema(request: ProblemaRequestModel):
    request = Problema.create(
        id_creyente=request.id_creyente,
        nombre_problema=request.nombre_problema,
        descripcion=request.descripcion,
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
            'nombre_problema': fila.nombre_problema,
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
            'nombre_problema': fila.nombre_problema,
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


def perfil(jid):
    try:
        problemas = Problema.select().join(Creyentes).join(Estados, on=(Problema.id_estado == Estados.id)).where(
            ((Creyentes.id == jid) & (Problema.activo == 1)) | ((Creyentes.id == 3) & (Problema.activo == 1))
        ).order_by(Problema.revision.asc())

        resultados = []

        for fila in problemas:
            creyente = Creyentes.get(Creyentes.id == fila.id_creyente.id)
            estado = Estados.get(Estados.id == fila.id_estado.id)
            modelo = {
                'id': fila.id,
                'id_creyente': fila.id_creyente.id,
                'nombre_creyente': creyente.nombre,
                'nombre_problema': fila.nombre_problema,
                'descripcion': fila.descripcion,
                'fecha_creacion': fila.fecha_creacion.strftime('%Y-%m-%dT%H:%M:%SZ'),
                'revision': fila.revision.strftime('%Y-%m-%dT%H:%M:%SZ'),
                'id_estado': fila.id_estado.id,
                'nombre_estado': estado.nombre,
                'activo': fila.activo
            }
            resultados.append(modelo)

        data = {
            'nombre_creyente': [creyente.nombre for creyente in Creyentes.select().where(Creyentes.id == jid)],
            'Problemas': resultados if resultados else None
        }

        return data

    except Exception as e:
        # Manejar la excepción adecuadamente, por ejemplo, imprimir un mensaje de error o registrar el problema.
        print(f"Error en la función perfil: {e}")
        return None



def cambiar_estado_problema(jid, id_estado):
    datos = Problema.select().where(Problema.id == jid).first()
    if datos:
        setattr(datos, 'id_estado', id_estado)
        datos.save()
        return 'exito'
    return 'error'


def cambiar_revision_problema(jid, revision):
    datos = Problema.select().where(Problema.id == jid).first()
    if datos:
        setattr(datos, 'revision', revision)
        datos.save()
        return 'exito'
    return 'error'


# **********************************************************************
