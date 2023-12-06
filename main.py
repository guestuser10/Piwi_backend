import json
from json import dumps
from peewee import *
from starlette.middleware.cors import CORSMiddleware

from database import *
from schemas import GruposRequestModel
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from apps.connector import *

app = FastAPI(
    title='pds',
    description='api para german',
    version='1.0'
)

origins = [
    "http://localhost",
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ********************************************************************************************
# events
@app.on_event("startup")
def startup():
    if database.is_closed():
        database.connect()


@app.on_event("shutdown")
def shutdown():
    if not database.is_closed():
        database.close()


# ********************************************************************************************
# requests
@app.get("/")
async def root():
    return {"message": "On service"}


# ********************************************************************************************
# login
Oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post('/token')
async def token(request_login: OAuth2PasswordRequestForm = Depends()):
    return await login_user(request_login)


# ********************************************************************************************
# CRUD grupo
# Insert
@app.post("/create_grupo")
async def create_grupo(request: GruposRequestModel):
    return crear_grupo(request)


# select
@app.post("/select_grupo")
async def select_grupo():
    return buscar_grupos()


# eliminar
@app.put("/desactivar_grupo/{jid}")
async def desactivar_grupo(jid, request_login: str = Depends(Oauth2_scheme)):
    return elimnar_grupo(jid)


# ********************************************************************************************
# CRUD Obreros
# Insert
@app.post("/create_obrero")
async def create_obrero(request: ObrerosRequestModel):
    return crear_obrero(request)


# select
@app.post("/select_obrero")
async def select_obrero():
    return buscar_obreros()


# eliminar
@app.put("/desactivar_obrero/{jid}")
async def desactivar_obrero(jid):
    return elimnar_obrero(jid)


@app.get("/search_obrero/{usuario}")
async def search_obrero(usuario):
    return buscar_obrero_por_usuario(usuario)
# ********************************************************************************************
# CRUD Creyentes
# Insert
@app.post("/create_Creyentes")
async def create_creyentes(request: CreyentesRequestModel):
    return crear_creyentes(request)


# select
@app.post("/select_Creyentes")
async def select_creyentes():
    return buscar_creyentes()


# eliminar
@app.put("/desactivar_Creyentes/{jid}")
async def desactivar_creyentes(jid):
    return elimnar_creyentes(jid)

@app.get("/search_Creyente/{jid}")
async def search_creyente(jid):
    return buscar_creyente_por_id(jid)


# ********************************************************************************************
# CRUD estados
# Insert
@app.post("/create_estado")
async def create_estado(request: GruposRequestModel):
    return crear_estado(request)


# select
@app.post("/select_estados")
async def select_estados():
    return buscar_estados()


# eliminar
@app.put("/desactivar_estado/{jid}")
async def desactivar_estado(jid):
    return elimnar_estado(jid)


# ********************************************************************************************
# CRUD Problemas
# Insert
@app.post("/create_problema")
async def create_problema(request: ProblemaRequestModel):
    return crear_problema(request)


# select
@app.post("/select_problemas")
async def select_problemas():
    return buscar_problemas()


# eliminar
@app.put("/desactivar_problema/{jid}")
async def desactivar_problema(jid):
    return elimnar_problema(jid)


# ********************************************************************************************
# CRUD Problemas
# Insert
@app.post("/create_mensaje")
async def create_mensaje(request: MensajesRequestModel):
    return crear_mensaje(request)


# buscar
@app.post("/select_mensajes")
async def select_mensajes():
    return buscar_mensajes()


# eliminar
@app.put("/desactivar_mensaje/{jid}")
async def desactivar_mensaje(jid):
    return eliminar_mensaje(jid)


# eliminar
@app.get("/conversacion/{jid}")
async def conversacion(jid):
    return buscar_conversacion(jid)


# ****************************************************************************
# buscar
@app.get("/main_menu/{jid}")
async def Main_menu(jid):
    return main_menu(jid)


@app.get("/perfil/{jid}")
async def obtener_perfil(jid):
    return perfil(jid)


@app.get("/miembros/{search_text}")
async def buscar_miembro(search_text):
    return barra_busqueda_miembros(search_text)


@app.get("/obreros/{search_text}")
async def buscar_obrero(search_text):
    return barra_busqueda_obreros(search_text)


@app.put("/estado/{jid}/{estado_id}")
async def cambiar_estado(jid, estado_id):
    return cambiar_estado_problema(jid, estado_id)


@app.put("/revision/{jid}/{revision}")
async def cambiar_revision(jid, revision):
    return cambiar_revision_problema(jid, revision)

# ****************************************************************************
# faq
@app.get("/faq")
async def faq():
    return get_faq()
