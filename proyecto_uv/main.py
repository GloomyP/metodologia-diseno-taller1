from repositories.memory import InMemoryRepository
from services.alumno_service import AlumnoService
from services.asignatura_service import AsignaturaService
from menu import ejecutar_sistema

def main():
    # Configuración inicial
    repo = InMemoryRepository()
    alumno_service = AlumnoService(repo)
    asignatura_service = AsignaturaService(repo)
    
    # Ejecutar el sistema con el menú interactivo
    ejecutar_sistema(alumno_service, asignatura_service)

if __name__ == "__main__":
    main()