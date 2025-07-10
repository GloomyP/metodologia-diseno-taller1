from abc import ABC, abstractmethod
from typing import List, Dict, Optional

class DatabaseRepository(ABC):
    @abstractmethod
    def save(self, entity: dict) -> None:
        pass
    
    @abstractmethod
    def get(self, id: str) -> Optional[dict]:
        pass
    
    @abstractmethod
    def get_all(self) -> List[dict]:
        pass
    
    @abstractmethod
    def update(self, id: str, entity: dict) -> None:
        pass
    
    @abstractmethod
    def delete(self, id: str) -> None:
        pass