from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class GruposRequestModel(BaseModel):
    nombre: str
    activo: int


class ObrerosRequestModel(BaseModel):
    nombre: str
    telefono: str
    direccion: str
    id_grupo: int
    activo: int
    usuario: str
    contrasena: str


class CreyentesRequestModel(BaseModel):
    nombre: str
    telefono: str
    direccion: str
    dias_disp: str
    id_grupo: int
    activo: int


class EstadosRequestModel(BaseModel):
    nombre: str
    activo: int


class ProblemaRequestModel(BaseModel):
    id_creyente: int
    nombre_problema: str
    descripcion: str
    fecha_creacion: datetime
    revision: datetime
    id_estado: int
    activo: int


class MensajesRequestModel(BaseModel):
    mensaje: str
    id_problema: int
    activo: int


class GruposResponseModel(GruposRequestModel):
    id: int


class ObrerosResponseModel(ObrerosRequestModel):
    id: int


class CreyentesResponseModel(CreyentesRequestModel):
    id: int


class EstadosResponseModel(EstadosRequestModel):
    id: int


class ProblemaResponseModel(ProblemaRequestModel):
    id: int


class MensajesResponseModel(MensajesRequestModel):
    id: int


