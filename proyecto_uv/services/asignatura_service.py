from typing import Dict, Optional
from models.asignatura import Asignatura
from repositories.base import DatabaseRepository

class AsignaturaService:
    def __init__(self, repository: DatabaseRepository):
        self.repository = repository
    
    def crear_asignatura(self, asignatura_data: dict) -> Asignatura:
        asignatura = Asignatura(
            asignatura_data['nombre'],
            asignatura_data['codigo'],
            asignatura_data['creditos'],
            asignatura_data.get('nivel', 'pregrado')
        )
        asignatura_dict = asignatura.to_dict()
        asignatura_dict['id'] = asignatura.codigo
        self.repository.save(asignatura_dict)
        return asignatura
    
    def obtener_asignatura(self, codigo: str) -> Optional[Asignatura]:
        asignatura_data = self.repository.get(codigo)
        if not asignatura_data:
            return None
        return Asignatura(
            asignatura_data['nombre'],
            asignatura_data['codigo'],
            asignatura_data['creditos'],
            asignatura_data.get('nivel', 'pregrado')
        )
    
def actualizar_asignatura(self, codigo: str, asignatura_data: dict) -> Optional[Asignatura]:
    existing_data = self.repository.get(codigo)
    if not existing_data:
        return None
    
    # Preparar datos actualizados
    updated_data = {
        'id': codigo,
        'nombre': asignatura_data.get('nombre', existing_data['nombre']),
        'codigo': codigo,
        'creditos': asignatura_data.get('creditos', existing_data['creditos']),
        'nivel': asignatura_data.get('nivel', existing_data.get('nivel', 'pregrado'))
    }
    
    self.repository.update(codigo, updated_data)
    return Asignatura(
        updated_data['nombre'],
        updated_data['codigo'],
        updated_data['creditos'],
        updated_data['nivel']
    )

def eliminar_asignatura(self, codigo: str) -> bool:
    if self.repository.get(codigo):
        self.repository.delete(codigo)
        return True
    return False
