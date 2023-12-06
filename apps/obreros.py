import json

from peewee import DoesNotExist

from database import obreros
from database import obreros as Obreros
from schemas import ObrerosRequestModel

import jwt
from fastapi import HTTPException
from datetime import datetime, timedelta


def crear_obrero(request: ObrerosRequestModel):
    request = obreros.create(
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
    request = obreros.select().where(obreros.activo == 1)
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
    datos = obreros.select().where(obreros.id == jid).first()
    if datos:
        setattr(datos, 'activo', 0)
        datos.save()
        return 'exito'
    return 'error'


def barra_busqueda_obreros(search_text):
    request = obreros.select().where(obreros.activo == 1 and obreros.nombre.contains(search_text))
    resultados = []
    for fila in request:
        modelo = {
            'id': fila.id,
            'nombre': fila.nombre,
            'telefono': fila.telefono,
            'direccion': fila.direccion,
            'id_grupo': fila.id_grupo.id,
            'activo': fila.activo,
        }
        resultados.append(modelo)
    json_result = json.dumps({'Obreros': resultados})
    data = json.loads(json_result)
    return data


# ************************************************************************************************
# login
SECRET_KEY = "177013"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


async def login_user(request_login):
    # Verifica las credenciales del usuario
    username = request_login.username
    password = request_login.password
    token = await authenticate_user(username, password)
    return {"access_token": token, "token_type": "bearer"}


async def authenticate_user(username: str, password: str):

    obreros = Obreros.get_or_none(Obreros.usuario == username and Obreros.contrasena == password)

    if obreros is None or not Obreros.contrasena == password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token_expires = timedelta(seconds=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token_data = {
        "sub": obreros.usuario,
        "exp": datetime.utcnow() + access_token_expires,
    }
    access_token = jwt.encode(access_token_data, SECRET_KEY, algorithm=ALGORITHM)

    return access_token


def buscar_obrero_por_usuario(usuario_buscar):
    try:
        obrero = obreros.get((obreros.usuario == usuario_buscar) & (obreros.activo == 1))
        modelo = {
            'id_grupo': obrero.id_grupo.id,
        }
        json_result = json.dumps({'Obrero': modelo})
        data = json.loads(json_result)
        return data
    except DoesNotExist:
        return {'mensaje': 'Usuario no encontrado'}