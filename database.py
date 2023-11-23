from datetime import datetime, timedelta

from peewee import *

database = MySQLDatabase(
    'backend',
    user='sealehen',
    password='1234',
    host='localhost',
    port=3306
)


class Grupos(Model):
    id = IntegerField()
    nombre = CharField(max_length=255)
    activo = IntegerField(default=1)

    class Meta:
        database = database
        table_name = 'Grupos'

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Activo: {self.activo}"


class Obreros(Model):
    id = IntegerField()
    nombre = CharField(max_length=255)
    telefono = CharField(max_length=255)
    direccion = CharField(max_length=255)
    id_grupo = ForeignKeyField(Grupos, field='id', backref='obreros', column_name='id_grupo')
    activo = IntegerField(default=1)
    usuario = CharField(max_length=255)
    contrasena = CharField(max_length=255)

    class Meta:
        database = database
        table_name = 'Obreros'

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Teléfono: {self.telefono}, Activo: {self.activo}"


class Creyentes(Model):
    id = IntegerField()
    nombre = CharField(max_length=255)
    telefono = CharField(max_length=255)
    direccion = TextField()
    dias_disp = CharField(max_length=255)
    id_grupo = ForeignKeyField(Grupos,  field='id', backref='creyentes', column_name='id_grupo')
    activo = IntegerField(default=1)

    class Meta:
        database = database
        table_name = 'Creyentes'

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Teléfono: {self.telefono}, Activo: {self.activo}"


class Estados(Model):
    id = IntegerField()
    nombre = CharField(max_length=255)
    activo = IntegerField(default=1)

    class Meta:
        database = database
        table_name = 'Estados'

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Activo: {self.activo}"


class Problema(Model):
    id = IntegerField()
    id_creyente = ForeignKeyField(Creyentes, field='id', backref='problema', column_name='id_creyente')
    nombre_problema = CharField(max_length=50)
    descripcion = TextField()
    fecha_creacion = DateTimeField(default=datetime.now)
    revision = DateTimeField(default=(datetime.now() + timedelta(weeks=1)))
    id_estado = ForeignKeyField(Estados, field='id', backref='problema', column_name='id_estado')
    activo = IntegerField(default=1)

    class Meta:
        database = database
        table_name = 'Problema'

    def __str__(self):
        return f"ID: {self.id}, Descripción: {self.descripcion}, Activo: {self.activo}"


class Mensajes(Model):
    id = IntegerField()
    mensaje = TextField()
    fecha = DateTimeField(default=datetime.now)
    id_problema = ForeignKeyField(Problema, field='id', backref='mensajes', column_name='id_problema')
    activo = IntegerField(default=1)

    class Meta:
        database = database
        table_name = 'mensajes'

    def __str__(self):
        return f"ID: {self.id}, Mensaje: {self.mensaje}, Activo: {self.activo}"
