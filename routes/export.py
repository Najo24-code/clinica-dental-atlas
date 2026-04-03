"""CSV Export — generado por ATLAS CORE"""
import csv
import io
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from database import get_db
from models import User, Paciente, Cita, Tratamiento
from auth import get_current_user

router = APIRouter()

@router.get("/pacientes/csv")
def export_pacientes_csv(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    items = db.query(Paciente).filter(Paciente.owner_id == current_user.id).all()
    cols  = [c.key for c in Paciente.__table__.columns]
    buf   = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(cols)
    for item in items:
        writer.writerow([getattr(item, c, "") for c in cols])
    buf.seek(0)
    return StreamingResponse(
        io.BytesIO(buf.getvalue().encode("utf-8")),
        media_type="text/csv; charset=utf-8",
        headers={"Content-Disposition": "attachment; filename=pacientes.csv"}
    )

@router.get("/citas/csv")
def export_citas_csv(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    items = db.query(Cita).filter(Cita.owner_id == current_user.id).all()
    cols  = [c.key for c in Cita.__table__.columns]
    buf   = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(cols)
    for item in items:
        writer.writerow([getattr(item, c, "") for c in cols])
    buf.seek(0)
    return StreamingResponse(
        io.BytesIO(buf.getvalue().encode("utf-8")),
        media_type="text/csv; charset=utf-8",
        headers={"Content-Disposition": "attachment; filename=citas.csv"}
    )

@router.get("/tratamientos/csv")
def export_tratamientos_csv(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    items = db.query(Tratamiento).filter(Tratamiento.owner_id == current_user.id).all()
    cols  = [c.key for c in Tratamiento.__table__.columns]
    buf   = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(cols)
    for item in items:
        writer.writerow([getattr(item, c, "") for c in cols])
    buf.seek(0)
    return StreamingResponse(
        io.BytesIO(buf.getvalue().encode("utf-8")),
        media_type="text/csv; charset=utf-8",
        headers={"Content-Disposition": "attachment; filename=tratamientos.csv"}
    )
