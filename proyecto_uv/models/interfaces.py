from abc import ABC, abstractmethod

class EstudianteBehavior(ABC):
    @abstractmethod
    def estudiar(self) -> str:
        pass

class AyudanteBehavior(ABC):
    @abstractmethod
    def hacer_ayudantia(self) -> str:
        pass

class ProfesorBehavior(ABC):
    @abstractmethod
    def hacer_clases(self) -> str:
        pass

class InvestigadorBehavior(ABC):
    @abstractmethod
    def investigar(self) -> str:
        pass

class NotasBehavior(ABC):
    @abstractmethod
    def descargar_notas(self) -> str:
        pass