from abc import ABC, abstractmethod
from typing import List, Optional
from .models import Pago

# Este es el "Puerto de Salida" (Secondary Port).
# Define un contrato (interfaz) que la lógica de negocio usará para
# comunicarse con el exterior (ej. una base de datos), sin saber
# los detalles de la implementación.

class PaymentRepositoryPort(ABC):
    """
    Puerto que define las operaciones de persistencia para los pagos.
    """

    @abstractmethod
    def save(self, pago: Pago) -> Pago:
        pass

    @abstractmethod
    def find_all(self) -> List[Pago]:
        pass

    @abstractmethod
    def find_by_id(self, pago_id: str) -> Optional[Pago]:
        pass

    @abstractmethod
    def find_by_client_name(self, nombre_cliente: str) -> List[Pago]:
        pass

    @abstractmethod
    def delete_by_id(self, pago_id: str) -> bool:
        pass