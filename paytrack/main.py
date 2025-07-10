import uvicorn
from infrastructure.adapters.rest_api import app

if __name__ == "__main__":
    # uvicorn.run espera el path al objeto de la app, en formato 'modulo:objeto'
    uvicorn.run("infrastructure.adapters.rest_api:app", host="127.0.0.1", port=8000, reload=True)