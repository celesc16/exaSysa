from app.models import Facultad
from app.repositories import FacultadRepository
class FacultadService:

  @staticmethod
  def crear_facultad(facultad: Facultad):
    FacultadRepository.crear_facultad(facultad)
    return facultad
  
  @staticmethod
  def listar_facultades():
    facultades= FacultadRepository.listar_facultades()
    return facultades

  def buscar_facultad(id: int):
    facultad = FacultadRepository.buscar_facultad(id)
    return facultad
    
  def actualizar_facultad(facultad: Facultad, id: int):
    facultad_existente = FacultadRepository.guardar_facultad(id)

    if not facultad_existente:
      return None
    
    facultad_existente = FacultadRepository.buscar_facultad(id)
    facultad_existente.nombre = facultad.nombre
    facultad_existente.abreviatura = facultad.abreviatura
    facultad_existente.directorio = facultad.directorio
    facultad_existente.sigla = facultad.sigla
    facultad_existente.codigoPostal = facultad.codigoPostal
    facultad_existente.ciudad = facultad.ciudad
    facultad_existente.domicilio = facultad.domicilio
    facultad_existente.telefono = facultad.telefono
    facultad_existente.contacto = facultad.contacto
    facultad_existente.email = facultad.email

    return FacultadRepository.guardar_facultad(facultad_existente)
  
  def eliminar_facultad(id: int):
    facultad = FacultadRepository.eliminar_facultad(id)
    
    
    