from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from auth import get_current_user
from models import User, Paciente, Cita
from schemas import CitaCreate, CitaResponse, CitaUpdate, PacienteCreate, PacienteResponse, PacienteUpdate

router = APIRouter()

@router.get("/", response_model=List[PacienteResponse])
def read_pacientes(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    pacientes = db.query(Paciente).filter(Paciente.owner_id == current_user.id).all()
    return pacientes

@router.post("/", response_model=PacienteResponse)
def create_paciente(paciente: PacienteCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_paciente = Paciente(nombre=paciente.nombre, apellido=paciente.apellido, fecha_nacimiento=paciente.fecha_nacimiento, owner_id=current_user.id)
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

@router.get("/{id}", response_model=PacienteResponse)
def read_paciente(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    paciente = db.query(Paciente).filter(Paciente.id == id).filter(Paciente.owner_id == current_user.id).first()
    if paciente is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente

@router.put("/{id}", response_model=PacienteResponse)
def update_paciente(id: int, paciente: PacienteUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_paciente = db.query(Paciente).filter(Paciente.id == id).filter(Paciente.owner_id == current_user.id).first()
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    if paciente.nombre:
        db_paciente.nombre = paciente.nombre
    if paciente.apellido:
        db_paciente.apellido = paciente.apellido
    if paciente.fecha_nacimiento:
        db_paciente.fecha_nacimiento = paciente.fecha_nacimiento
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

@router.delete("/{id}")
def delete_paciente(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    paciente = db.query(Paciente).filter(Paciente.id == id).filter(Paciente.owner_id == current_user.id).first()
    if paciente is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    db.delete(paciente)
    db.commit()
    return {"message": "Paciente eliminado"}

@router.get("/citas/", response_model=List[CitaResponse])
def read_citas(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    citas = db.query(Cita).filter(Cita.owner_id == current_user.id).all()
    return citas

@router.post("/citas/", response_model=CitaResponse)
def create_cita(cita: CitaCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_cita = Cita(fecha=cita.fecha, hora=cita.hora, paciente_id=cita.paciente_id, tratamiento=cita.tratamiento, owner_id=current_user.id)
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)
    return db_cita

@router.get("/citas/{id}", response_model=CitaResponse)
def read_cita(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    cita = db.query(Cita).filter(Cita.id == id).filter(Cita.owner_id == current_user.id).first()
    if cita is None:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita

@router.put("/citas/{id}", response_model=CitaResponse)
def update_cita(id: int, cita: CitaUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_cita = db.query(Cita).filter(Cita.id == id).filter(Cita.owner_id == current_user.id).first()
    if db_cita is None:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    if cita.fecha:
        db_cita.fecha = cita.fecha
    if cita.hora:
        db_cita.hora = cita.hora
    if cita.paciente_id:
        db_cita.paciente_id = cita.paciente_id
    if cita.tratamiento:
        db_cita.tratamiento = cita.tratamiento
    db.commit()
    db.refresh(db_cita)
    return db_cita

@router.delete("/citas/{id}")
def delete_cita(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    cita = db.query(Cita).filter(Cita.id == id).filter(Cita.owner_id == current_user.id).first()
    if cita is None:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    db.delete(cita)
    db.commit()
    return {"message": "Cita eliminada"}