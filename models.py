from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float, Text
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    pacientes = relationship("Paciente", back_populates="owner")
    citas = relationship("Cita", back_populates="owner")

class Paciente(Base):
    __tablename__ = "pacientes"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    fecha_nacimiento = Column(DateTime)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="pacientes")

class Cita(Base):
    __tablename__ = "citas"
    id = Column(Integer, primary_key=True)
    fecha = Column(DateTime)
    hora = Column(String)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    paciente = relationship("Paciente")
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="citas")
    tratamiento = relationship("Tratamiento", back_populates="cita")

class Tratamiento(Base):
    __tablename__ = "tratamientos"
    id = Column(Integer, primary_key=True)
    descripcion = Column(Text)
    costo = Column(Float)
    cita_id = Column(Integer, ForeignKey("citas.id"))
    cita = relationship("Cita", back_populates="tratamiento")
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User")