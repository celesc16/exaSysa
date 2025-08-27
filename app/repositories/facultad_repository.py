from app.models import Facultad
from app import db


class FacultadRepository:

  @staticmethod
  def crear_facultad(facultad: Facultad):
    db.session.add(facultad)
    db.session.commit()
    return facultad
  
  @staticmethod
  def listar_facultades() -> list[Facultad]:
    return db.session.query(Facultad).all()
  
  @staticmethod
  def buscar_facultad(id: int) -> Facultad:
    return db.session.query(Facultad).filter(Facultad.id == id).one_or_none()
  
  @staticmethod
  def guardar_facultad(facultad: Facultad, id: int) -> Facultad:
    db.session.commit()
    return facultad
  
  @staticmethod
  def eliminar_facultad(id: int) -> None:
    entity = FacultadRepository.buscar_facultad(id)
    db.session.delete(entity)
    db.session.commit()