from typing import List
from domain.models import Pago
from domain.ports import PaymentRepositoryPort

# Los casos de uso implementan la lógica de la aplicación.
# Dependen de las abstracciones (puertos) del dominio, no de las
# implementaciones concretas. Esto se logra mediante Inyección de Dependencias.

class RegisterPaymentUseCase:
    def __init__(self, repository: PaymentRepositoryPort):
        self.repository = repository

    def execute(self, nombre_cliente: str, monto: float) -> Pago:
        # La validación del monto ocurre en el constructor del modelo de dominio.
        nuevo_pago = Pago(nombre_cliente=nombre_cliente, monto=monto)
        return self.repository.save(nuevo_pago)

class ListPaymentsUseCase:
    def __init__(self, repository: PaymentRepositoryPort):
        self.repository = repository

    def execute(self) -> List[Pago]:
        return self.repository.find_all()

class FindPaymentsByClientUseCase:
    def __init__(self, repository: PaymentRepositoryPort):
        self.repository = repository

    def execute(self, nombre_cliente: str) -> List[Pago]:
        return self.repository.find_by_client_name(nombre_cliente)

class DeletePaymentUseCase:
    def __init__(self, repository: PaymentRepositoryPort):
        self.repository = repository

    def execute(self, pago_id: str) -> bool:
        pago = self.repository.find_by_id(pago_id)
        if not pago:
            raise ValueError("Pago no encontrado.")
        
        # Regla de negocio: solo se pueden eliminar pagos completados.
        if pago.estado != "COMPLETADO":
            raise PermissionError("No se puede eliminar un pago que no esté en estado 'COMPLETADO'.")
            
        return self.repository.delete_by_id(pago_id)