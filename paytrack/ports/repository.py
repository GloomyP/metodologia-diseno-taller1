from abc import ABC, abstractmethod
from typing import List
from paytrack.domain.models import Payment

class PaymentRepository(ABC):
    @abstractmethod
    def save(self, payment: Payment):
        pass

    @abstractmethod
    def get_all(self) -> List[Payment]:
        pass

    @abstractmethod
    def find_by_client(self, nombre_cliente: str) -> List[Payment]:
        pass

    @abstractmethod
    def delete(self, payment_id: str) -> bool:
        pass

    @abstractmethod
    def get_by_id(self, payment_id: str) -> Payment | None:
        pass
