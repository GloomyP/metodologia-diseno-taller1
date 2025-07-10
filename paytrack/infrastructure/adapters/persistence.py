from typing import List, Optional, Dict
from domain.models import Pago
from domain.ports import PaymentRepositoryPort

# Este es un "Adaptador de Salida" (Secondary Adapter).
# Implementa el puerto de persistencia usando una simple base de datos en memoria (un diccionario).
# Podríamos cambiar esto por un adaptador de SQL o NoSQL sin tocar el dominio o los casos de uso.

class InMemoryPaymentRepository(PaymentRepositoryPort):
    def __init__(self):
        self._pagos: Dict[str, Pago] = {}

    def save(self, pago: Pago) -> Pago:
        print(f"Guardando pago {pago.id} en memoria.")
        self._pagos[pago.id] = pago
        return pago

    def find_all(self) -> List[Pago]:
        return list(self._pagos.values())

    def find_by_id(self, pago_id: str) -> Optional[Pago]:
        return self._pagos.get(pago_id)

    def find_by_client_name(self, nombre_cliente: str) -> List[Pago]:
        # Búsqueda insensible a mayúsculas/minúsculas como sugiere el requisito.
        return [
            pago for pago in self._pagos.values() 
            if pago.nombre_cliente.lower() == nombre_cliente.lower()
        ]

    def delete_by_id(self, pago_id: str) -> bool:
        if pago_id in self._pagos:
            del self._pagos[pago_id]
            return True
        return False