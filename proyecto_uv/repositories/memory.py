from typing import List, Dict, Optional
from .base import DatabaseRepository

class InMemoryRepository(DatabaseRepository):
    def __init__(self):
        self._data = {}
    
    def save(self, entity: dict) -> None:
        self._data[entity['id']] = entity
        print(f"Guardando en base de datos: {entity}")
    
    def get(self, id: str) -> Optional[dict]:
        return self._data.get(id)
    
    def get_all(self) -> List[dict]:
        return list(self._data.values())
    
    def update(self, id: str, entity: dict) -> None:
        if id in self._data:
            self._data[id] = entity
            print(f"Actualizando en base de datos: {entity}")
    
    def delete(self, id: str) -> None:
        if id in self._data:
            del self._data[id]
            print(f"Eliminando de base de datos el ID: {id}")