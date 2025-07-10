import uuid
from datetime import datetime
from dataclasses import dataclass, field

# Usamos dataclasses para tener objetos de datos limpios y claros.
# Este es nuestro objeto principal del dominio.

@dataclass
class Pago:
    nombre_cliente: str
    monto: float
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    fecha: datetime = field(default_factory=datetime.utcnow)
    estado: str = "COMPLETADO"

    def __post_init__(self):
        """Valida las reglas de negocio después de la inicialización."""
        if self.monto <= 0:
            raise ValueError("El monto del pago debe ser mayor que cero.")