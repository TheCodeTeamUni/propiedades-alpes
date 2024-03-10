from propiedadesalpes.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()


class Propiedad(db.Model):
    __tablename__ = "propiedades"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    nombre = db.Column(db.String, nullable=False)
    descripcion = db.Column(db.String, nullable=False)
    tipo = db.Column(db.String, nullable=False)
    piso = db.Column(db.String, nullable=False)
    longitud = db.Column(db.String, nullable=False)
    latitud = db.Column(db.String, nullable=False)
