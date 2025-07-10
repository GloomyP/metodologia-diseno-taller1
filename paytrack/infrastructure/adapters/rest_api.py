from fastapi import FastAPI, HTTPException, status, Query
from pydantic import BaseModel
from typing import List

from application.use_cases import (
    RegisterPaymentUseCase,
    ListPaymentsUseCase,
    FindPaymentsByClientUseCase,
    DeletePaymentUseCase
)
from .persistence import InMemoryPaymentRepository

# Este es el "Adaptador de Entrada" (Primary Adapter).
# Expone la funcionalidad de la aplicación a través de una API REST usando FastAPI.

app = FastAPI(
    title="PayTrack API",
    description="Sistema para el registro, gestión y consulta de pagos.",
    version="1.0.0"
)

# --- Dependencias ---
# Se crea una única instancia del repositorio (singleton para esta demo).
payment_repository = InMemoryPaymentRepository()

# --- Modelos de datos para la API (DTOs) ---
# Modelo para la entrada de datos al registrar un pago.
class PaymentRequest(BaseModel):
    nombre_cliente: str
    monto: float

# Modelo para la salida de datos, asegurando que no se expongan detalles internos.
class PaymentResponse(BaseModel):
    id: str
    nombre_cliente: str
    monto: float
    fecha: str
    estado: str

# --- Endpoints de la API ---

@app.post("/pagos", status_code=status.HTTP_201_CREATED, response_model=PaymentResponse, tags=["Pagos"])
def register_payment(request: PaymentRequest):
    """RF1: Registra un nuevo pago."""
    try:
        use_case = RegisterPaymentUseCase(payment_repository)
        pago_registrado = use_case.execute(request.nombre_cliente, request.monto)
        # Formateamos la fecha a string para la respuesta JSON.
        return PaymentResponse(
            **pago_registrado.__dict__,
            fecha=pago_registrado.fecha.isoformat()
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@app.get("/pagos", response_model=List[PaymentResponse], tags=["Pagos"])
def list_all_payments():
    """RF2: Lista todos los pagos registrados."""
    use_case = ListPaymentsUseCase(payment_repository)
    pagos = use_case.execute()
    return [PaymentResponse(**p.__dict__, fecha=p.fecha.isoformat()) for p in pagos]

@app.get("/pagos/buscar", response_model=List[PaymentResponse], tags=["Pagos"])
def search_payments_by_client(nombre_cliente: str = Query(..., min_length=1)):
    """RF3: Busca pagos por nombre de cliente."""
    use_case = FindPaymentsByClientUseCase(payment_repository)
    pagos = use_case.execute(nombre_cliente)
    return [PaymentResponse(**p.__dict__, fecha=p.fecha.isoformat()) for p in pagos]

@app.delete("/pagos/{pago_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Pagos"])
def delete_payment(pago_id: str):
    """RF4: Elimina un pago por su ID."""
    try:
        use_case = DeletePaymentUseCase(payment_repository)
        use_case.execute(pago_id)
        # En éxito, no se retorna contenido.
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except PermissionError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))