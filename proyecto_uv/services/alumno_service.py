from datetime import date
from typing import Dict, Optional
from models import Alumno, AlumnoTitulado, AlumnoRegular, AlumnoAyudante, AlumnoMagister, AlumnoDoctorado
from models.asignatura import Asignatura
from repositories.base import DatabaseRepository

class AlumnoService:
    def __init__(self, repository: DatabaseRepository):
        self.repository = repository
    
    def crear_alumno(self, alumno_data: dict) -> Alumno:
        alumno = self._create_alumno_instance(alumno_data)
        alumno_dict = {
            'id': alumno_data['rut'],
            'nombre': alumno_data['nombre'],
            'edad': alumno_data['edad'],
            'rut': alumno_data['rut'],
            'fecha_nacimiento': alumno_data['fecha_nacimiento'].isoformat(),
            'tipo': alumno_data['tipo'],
            'asignaturas': [a.to_dict() for a in alumno.asignaturas]
        }
        self.repository.save(alumno_dict)
        return alumno
    
    def obtener_alumno(self, rut: str) -> Optional[Alumno]:
        alumno_data = self.repository.get(rut)
        if not alumno_data:
            return None
        return self._create_alumno_instance(alumno_data)
    
    def _create_alumno_instance(self, data: dict) -> Alumno:
        fecha_nac = date.fromisoformat(data['fecha_nacimiento']) if isinstance(data['fecha_nacimiento'], str) else data['fecha_nacimiento']
        
        tipo = data.get('tipo', 'regular')
        if tipo == 'titulado':
            alumno = AlumnoTitulado(data['nombre'], data['edad'], data['rut'], fecha_nac)
        elif tipo == 'regular':
            alumno = AlumnoRegular(data['nombre'], data['edad'], data['rut'], fecha_nac)
        elif tipo == 'ayudante':
            alumno = AlumnoAyudante(data['nombre'], data['edad'], data['rut'], fecha_nac)
        elif tipo == 'magister':
            alumno = AlumnoMagister(data['nombre'], data['edad'], data['rut'], fecha_nac)
        elif tipo == 'doctorado':
            alumno = AlumnoDoctorado(data['nombre'], data['edad'], data['rut'], fecha_nac)
        else:
            alumno = AlumnoRegular(data['nombre'], data['edad'], data['rut'], fecha_nac)
        
        if 'asignaturas' in data:
            for a_data in data['asignaturas']:
                asignatura = Asignatura(
                    a_data['nombre'],
                    a_data['codigo'],
                    a_data['creditos'],
                    a_data.get('nivel', 'pregrado')
                )
                alumno.agregar_asignatura(asignatura)
        
        return alumno
    
def actualizar_alumno(self, rut: str, alumno_data: dict) -> Optional[Alumno]:
    existing_data = self.repository.get(rut)
    if not existing_data:
        return None
    
    # Preparar datos actualizados
    updated_data = {
        'id': rut,
        'nombre': alumno_data.get('nombre', existing_data['nombre']),
        'edad': alumno_data.get('edad', existing_data['edad']),
        'rut': rut,
        'fecha_nacimiento': existing_data['fecha_nacimiento'],  # No permitimos cambiar esto
        'tipo': alumno_data.get('tipo', existing_data['tipo']),
        'asignaturas': existing_data['asignaturas']  # Mantener las existentes
    }
    
    self.repository.update(rut, updated_data)
    return self._create_alumno_instance(updated_data)

def eliminar_alumno(self, rut: str) -> bool:
    if self.repository.get(rut):
        self.repository.delete(rut)
        return True
    return False
