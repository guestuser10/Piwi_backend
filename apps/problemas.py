import json
from database import problema, creyentes, estados
from schemas import ProblemaRequestModel, ProblemaResponseModel


def crear_problema(request: ProblemaRequestModel):
    request = problema.create(
        id_creyente=request.id_creyente,
        nombre_problema=request.nombre_problema,
        descripcion=request.descripcion,
        id_estado=request.id_estado,
        activo=request.activo,
    )
    return request


def buscar_problemas():
    request = problema.select().where(problema.activo == 1).order_by(problema.revision.asc())
    resultados = []

    for fila in request:
        creyente = creyentes.get(creyentes.id == fila.id_creyente.id)
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
    datos = problema.select().where(problema.id == jid).first()
    if datos:
        setattr(datos, 'activo', 0)
        datos.save()
        return 'exito'
    return 'error'

def main_menu(gpo):
    problema = problema.select().join(creyentes).where(
        ((creyentes.id_grupo == gpo) & (problema.activo == 1)) | ((creyentes.id_grupo == 3) & (problema.activo == 1))
    ).order_by(problema.revision.asc())

    resultados = []

    for fila in problema:
        creyente = creyentes.get(creyentes.id == fila.id_creyente.id)
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
        problemas = problema.select().join(creyentes).join(estados, on=(problema.id_estado == estados.id)).where(
            ((creyentes.id == jid) & (problema.activo == 1)) | ((creyentes.id == 3) & (problema.activo == 1))
        ).order_by(problema.revision.asc())

        resultados = []

        for fila in problemas:
            creyente = creyentes.get(creyentes.id == fila.id_creyente.id)
            estado = estados.get(estados.id == fila.id_estado.id)
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
            'nombre_creyente': [creyente.nombre for creyente in creyentes.select().where(creyentes.id == jid)],
            'Problemas': resultados if resultados else None
        }

        return data

    except Exception as e:
        # Manejar la excepción adecuadamente, por ejemplo, imprimir un mensaje de error o registrar el problema.
        print(f"Error en la función perfil: {e}")
        return None



def cambiar_estado_problema(jid, id_estado):
    datos = problema.select().where(problema.id == jid).first()
    if datos:
        setattr(datos, 'id_estado', id_estado)
        datos.save()
        return 'exito'
    return 'error'


def cambiar_revision_problema(jid, revision):
    datos = problema.select().where(problema.id == jid).first()
    if datos:
        setattr(datos, 'revision', revision)
        datos.save()
        return 'exito'
    return 'error'


# **********************************************************************
