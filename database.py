from datetime import datetime, timedelta

from peewee import *

database = MySQLDatabase(
    'buecxuea9f2lqjuodwnu',
    user='uzltr9cv3fug4ubo',
    password='fTJtX0E4q5iFgOA89CSz',
    host='buecxuea9f2lqjuodwnu-mysql.services.clever-cloud.com',
    port=3306
)
""" 
'backend',
    'backend',
    user='sealehen',
    password='1234',
    host='localhost',
"""

class grupos(Model):
    id = IntegerField()
    nombre = CharField(max_length=255)
    activo = IntegerField(default=1)

    class Meta:
        database = database
        table_name = 'grupos'

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Activo: {self.activo}"


class obreros(Model):
    id = IntegerField()
    nombre = CharField(max_length=255)
    telefono = CharField(max_length=255)
    direccion = CharField(max_length=255)
    id_grupo = ForeignKeyField(grupos, field='id', backref='obreros', column_name='id_grupo')
    activo = IntegerField(default=1)
    usuario = CharField(max_length=255)
    contrasena = CharField(max_length=255)

    class Meta:
        database = database
        table_name = 'obreros'

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Teléfono: {self.telefono}, Activo: {self.activo}"


class creyentes(Model):
    id = IntegerField()
    nombre = CharField(max_length=255)
    telefono = CharField(max_length=255)
    direccion = TextField()
    dias_disp = CharField(max_length=255)
    id_grupo = ForeignKeyField(grupos, field='id', backref='creyentes', column_name='id_grupo')
    activo = IntegerField(default=1)

    class Meta:
        database = database
        table_name = 'creyentes'

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Teléfono: {self.telefono}, Activo: {self.activo}"


class estados(Model):
    id = IntegerField()
    nombre = CharField(max_length=255)
    activo = IntegerField(default=1)

    class Meta:
        database = database
        table_name = 'estados'

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Activo: {self.activo}"


class problema(Model):
    id = IntegerField()
    id_creyente = ForeignKeyField(creyentes, field='id', backref='problema', column_name='id_creyente')
    nombre_problema = CharField(max_length=50)
    descripcion = TextField()
    fecha_creacion = DateTimeField(default=datetime.now)
    revision = DateTimeField(default=(datetime.now() + timedelta(weeks=1)))
    id_estado = ForeignKeyField(estados, field='id', backref='problema', column_name='id_estado')
    activo = IntegerField(default=1)

    class Meta:
        database = database
        table_name = 'problema'

    def __str__(self):
        return f"ID: {self.id}, Descripción: {self.descripcion}, Activo: {self.activo}"


class mensajes(Model):
    id = IntegerField()
    mensaje = TextField()
    fecha = DateTimeField(default=datetime.now)
    id_problema = ForeignKeyField(problema, field='id', backref='mensajes', column_name='id_problema')
    activo = IntegerField(default=1)

    class Meta:
        database = database
        table_name = 'mensajes'

    def __str__(self):
        return f"ID: {self.id}, Mensaje: {self.mensaje}, Activo: {self.activo}"


class faq(Model):
    id = IntegerField()
    ask = TextField()
    answer = TextField()

    class Meta:
        database = database
        table_name = 'faq'

    def __str__(self):
        return f"ID: {self.id}, ask: {self.ask}, answer: {self.answer}"
