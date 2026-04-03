from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    is_active: bool

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class PacienteCreate(BaseModel):
    nombre: str
    apellido: str
    fecha_nacimiento: datetime

class PacienteUpdate(BaseModel):
    nombre: Optional[str]
    apellido: Optional[str]
    fecha_nacimiento: Optional[datetime]

class PacienteResponse(BaseModel):
    id: int
    owner_id: int
    nombre: str
    apellido: str
    fecha_nacimiento: datetime

    class Config:
        from_attributes = True

class CitaCreate(BaseModel):
    fecha: datetime
    hora: str
    paciente_id: int
    tratamiento: Optional[str]

class CitaUpdate(BaseModel):
    fecha: Optional[datetime]
    hora: Optional[str]
    paciente_id: Optional[int]
    tratamiento: Optional[str]

class CitaResponse(BaseModel):
    id: int
    owner_id: int
    fecha: datetime
    hora: str
    paciente_id: int
    tratamiento: Optional[str]

    class Config:
        from_attributes = True

class TratamientoCreate(BaseModel):
    descripcion: str

class TratamientoUpdate(BaseModel):
    descripcion: Optional[str]

class TratamientoResponse(BaseModel):
    id: int
    owner_id: int
    descripcion: str

    class Config:
        from_attributes = True