from datetime import date
import sys
from typing import Optional
from models.alumno import Alumno
from models.asignatura import Asignatura
from services.alumno_service import AlumnoService
from services.asignatura_service import AsignaturaService
from repositories.base import DatabaseRepository


def mostrar_menu_principal():
    print("\n=== Sistema Gestión UV ===")
    print("1. Gestión de Alumnos")
    print("2. Gestión de Asignaturas")
    print("3. Acciones específicas (notas, etc.)")
    print("4. Salir")
    return input("Seleccione una opción: ")

from datetime import date
import sys
from typing import Optional
from models.alumno import Alumno
from models.asignatura import Asignatura

def mostrar_menu_principal():
    print("\n=== Sistema Gestión UV ===")
    print("1. Gestión de Alumnos")
    print("2. Gestión de Asignaturas")
    print("3. Acciones específicas (notas, etc.)")
    print("4. Salir")
    return input("Seleccione una opción: ")

def mostrar_menu_alumnos():
    print("\n--- Gestión de Alumnos ---")
    print("1. Crear alumno")
    print("2. Buscar alumno por RUT")
    print("3. Actualizar alumno")
    print("4. Eliminar alumno")
    print("5. Listar todos los alumnos")
    print("6. Volver al menú principal")
    return input("Seleccione una opción: ")

def mostrar_menu_asignaturas():
    print("\n--- Gestión de Asignaturas ---")
    print("1. Crear asignatura")
    print("2. Buscar asignatura por código")
    print("3. Actualizar asignatura")
    print("4. Eliminar asignatura")
    print("5. Listar todas las asignaturas")
    print("6. Volver al menú principal")
    return input("Seleccione una opción: ")

def mostrar_menu_acciones():
    print("\n--- Acciones Específicas ---")
    print("1. Descargar notas de alumno")
    print("2. Realizar acción según tipo de alumno")
    print("3. Volver al menú principal")
    return input("Seleccione una opción: ")

def crear_alumno_interactivo(service) -> Optional[Alumno]:
    try:
        print("\nCrear nuevo alumno:")
        tipo = input("Tipo (regular/ayudante/magister/doctorado/titulado): ").lower()
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        rut = input("RUT (sin puntos con guión): ")
        fecha_str = input("Fecha nacimiento (YYYY-MM-DD): ")
        año, mes, dia = map(int, fecha_str.split('-'))
        
        alumno_data = {
            'nombre': nombre,
            'edad': edad,
            'rut': rut,
            'fecha_nacimiento': date(año, mes, dia),
            'tipo': tipo,
            'asignaturas': []
        }
        
        alumno = service.crear_alumno(alumno_data)
        print(f"\nAlumno creado exitosamente: {alumno}")
        return alumno
    except ValueError as e:
        print(f"\nError: {e}")
        return None

def buscar_alumno_interactivo(service) -> Optional[Alumno]:
    rut = input("\nIngrese RUT del alumno a buscar: ")
    alumno = service.obtener_alumno(rut)
    if alumno:
        print(f"\nDatos del alumno:")
        print(f"Nombre: {alumno.nombre}")
        print(f"RUT: {alumno.rut}")
        print(f"Edad: {alumno.edad}")
        print(f"Tipo: {type(alumno).__name__}")
        print(f"Asignaturas inscritas: {len(alumno.asignaturas)}")
        for asignatura in alumno.asignaturas:
            print(f"  - {asignatura}")
    else:
        print("\nAlumno no encontrado")
    return alumno

def actualizar_alumno_interactivo(service):
    rut = input("\nIngrese RUT del alumno a actualizar: ")
    alumno = service.obtener_alumno(rut)
    
    if not alumno:
        print("\nAlumno no encontrado")
        return
    
    print("\nDeje en blanco los campos que no desea modificar")
    nombre = input(f"Nuevo nombre ({alumno.nombre}): ") or alumno.nombre
    edad = input(f"Nueva edad ({alumno.edad}): ")
    edad = int(edad) if edad else alumno.edad
    tipo = input(f"Nuevo tipo ({type(alumno).__name__.lower()}): ") or alumno.tipo
    
    update_data = {
        'nombre': nombre,
        'edad': edad,
        'tipo': tipo,
        'rut': rut
    }
    
    updated = service.actualizar_alumno(rut, update_data)
    if updated:
        print("\nAlumno actualizado exitosamente:")
        print(updated)
    else:
        print("\nError al actualizar alumno")

def eliminar_alumno_interactivo(service):
    rut = input("\nIngrese RUT del alumno a eliminar: ")
    if service.eliminar_alumno(rut):
        print("\nAlumno eliminado exitosamente")
    else:
        print("\nAlumno no encontrado")

def listar_alumnos(service):
    print("\nListado de todos los alumnos:")
    alumnos = [service.obtener_alumno(alumno['rut']) for alumno in service.repository.get_all() if 'rut' in alumno]
    for alumno in alumnos:
        if alumno:
            print(f"- {alumno}")

def crear_asignatura_interactivo(service):
    try:
        print("\nCrear nueva asignatura:")
        nombre = input("Nombre: ")
        codigo = input("Código: ")
        creditos = int(input("Créditos: "))
        nivel = input("Nivel (pregrado/magister/doctorado): ").lower()
        
        asignatura = service.crear_asignatura({
            'nombre': nombre,
            'codigo': codigo,
            'creditos': creditos,
            'nivel': nivel
        })
        print(f"\nAsignatura creada exitosamente: {asignatura}")
    except ValueError as e:
        print(f"\nError: {e}")

def buscar_asignatura_interactivo(service):
    codigo = input("\nIngrese código de la asignatura a buscar: ")
    asignatura = service.obtener_asignatura(codigo)
    if asignatura:
        print(f"\nDatos de la asignatura:")
        print(asignatura)
    else:
        print("\nAsignatura no encontrada")

def actualizar_asignatura_interactivo(service):
    codigo = input("\nIngrese código de la asignatura a actualizar: ")
    asignatura = service.obtener_asignatura(codigo)
    
    if not asignatura:
        print("\nAsignatura no encontrada")
        return
    
    print("\nDeje en blanco los campos que no desea modificar")
    nombre = input(f"Nuevo nombre ({asignatura.nombre}): ") or asignatura.nombre
    creditos = input(f"Nuevos créditos ({asignatura.creditos}): ")
    creditos = int(creditos) if creditos else asignatura.creditos
    nivel = input(f"Nuevo nivel ({asignatura.nivel}): ") or asignatura.nivel
    
    update_data = {
        'nombre': nombre,
        'creditos': creditos,
        'nivel': nivel,
        'codigo': codigo
    }
    
    updated = service.actualizar_asignatura(codigo, update_data)
    if updated:
        print("\nAsignatura actualizada exitosamente:")
        print(updated)
    else:
        print("\nError al actualizar asignatura")

def eliminar_asignatura_interactivo(service):
    codigo = input("\nIngrese código de la asignatura a eliminar: ")
    if service.eliminar_asignatura(codigo):
        print("\nAsignatura eliminada exitosamente")
    else:
        print("\nAsignatura no encontrada")

def listar_asignaturas(service):
    print("\nListado de todas las asignaturas:")
    asignaturas = [service.obtener_asignatura(asig['codigo']) for asig in service.repository.get_all() if 'codigo' in asig]
    for asignatura in asignaturas:
        if asignatura:
            print(f"- {asignatura}")

def descargar_notas_interactivo(service):
    rut = input("\nIngrese RUT del alumno para descargar notas: ")
    alumno = service.obtener_alumno(rut)
    if alumno:
        print(f"\n{alumno.descargar_notas()}")
    else:
        print("\nAlumno no encontrado")

def acciones_especificas_interactivo(service):
    rut = input("\nIngrese RUT del alumno: ")
    alumno = service.obtener_alumno(rut)
    
    if not alumno:
        print("\nAlumno no encontrado")
        return
    
    print(f"\nAcciones disponibles para {alumno.nombre} ({type(alumno).__name__}):")
    
    if hasattr(alumno, 'estudiar'):
        print("1. Estudiar")
    if hasattr(alumno, 'hacer_ayudantia'):
        print("2. Hacer ayudantía")
    if hasattr(alumno, 'hacer_clases'):
        print("3. Hacer clases")
    if hasattr(alumno, 'investigar'):
        print("4. Investigar")
    
    opcion = input("Seleccione acción a realizar: ")
    
    if opcion == "1" and hasattr(alumno, 'estudiar'):
        print(alumno.estudiar())
    elif opcion == "2" and hasattr(alumno, 'hacer_ayudantia'):
        print(alumno.hacer_ayudantia())
    elif opcion == "3" and hasattr(alumno, 'hacer_clases'):
        print(alumno.hacer_clases())
    elif opcion == "4" and hasattr(alumno, 'investigar'):
        print(alumno.investigar())
    else:
        print("\nOpción no válida o acción no disponible para este tipo de alumno")

def manejar_menu_alumnos(service):
    while True:
        opcion = mostrar_menu_alumnos()
        
        if opcion == "1":
            crear_alumno_interactivo(service)
        elif opcion == "2":
            buscar_alumno_interactivo(service)
        elif opcion == "3":
            actualizar_alumno_interactivo(service)
        elif opcion == "4":
            eliminar_alumno_interactivo(service)
        elif opcion == "5":
            listar_alumnos(service)
        elif opcion == "6":
            break
        else:
            print("\nOpción no válida, intente nuevamente")

def manejar_menu_asignaturas(service):
    while True:
        opcion = mostrar_menu_asignaturas()
        
        if opcion == "1":
            crear_asignatura_interactivo(service)
        elif opcion == "2":
            buscar_asignatura_interactivo(service)
        elif opcion == "3":
            actualizar_asignatura_interactivo(service)
        elif opcion == "4":
            eliminar_asignatura_interactivo(service)
        elif opcion == "5":
            listar_asignaturas(service)
        elif opcion == "6":
            break
        else:
            print("\nOpción no válida, intente nuevamente")

def manejar_menu_acciones(service):
    while True:
        opcion = mostrar_menu_acciones()
        
        if opcion == "1":
            descargar_notas_interactivo(service)
        elif opcion == "2":
            acciones_especificas_interactivo(service)
        elif opcion == "3":
            break
        else:
            print("\nOpción no válida, intente nuevamente")

def ejecutar_sistema(alumno_service, asignatura_service):
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == "1":
            manejar_menu_alumnos(alumno_service)
        elif opcion == "2":
            manejar_menu_asignaturas(asignatura_service)
        elif opcion == "3":
            manejar_menu_acciones(alumno_service)
        elif opcion == "4":
            print("\nSaliendo del sistema...")
            sys.exit()
        else:
            print("\nOpción no válida, intente nuevamente")
