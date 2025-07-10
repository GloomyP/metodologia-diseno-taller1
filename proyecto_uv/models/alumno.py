from datetime import date
from typing import List, Optional
from .asignatura import Asignatura
from .interfaces import EstudianteBehavior, AyudanteBehavior, ProfesorBehavior, InvestigadorBehavior, NotasBehavior

class Alumno(NotasBehavior):
    def __init__(self, nombre: str, edad: int, rut: str, fecha_nacimiento: date):
        self.nombre = nombre
        self.edad = edad
        self.rut = rut
        self.fecha_nacimiento = fecha_nacimiento
        self.asignaturas: List[Asignatura] = []
    
    def agregar_asignatura(self, asignatura: Asignatura) -> None:
        self.asignaturas.append(asignatura)
    
    def eliminar_asignatura(self, codigo: str) -> None:
        self.asignaturas = [a for a in self.asignaturas if a.codigo != codigo]
    
    def get_asignatura(self, codigo: str) -> Optional[Asignatura]:
        return next((a for a in self.asignaturas if a.codigo == codigo), None)
    
    def descargar_notas(self) -> str:
        return f"Notas descargadas para {self.nombre} ({self.rut})"
    
    def __str__(self):
        return f"{self.nombre} ({self.rut}) - {len(self.asignaturas)} asignaturas"

class AlumnoTitulado(Alumno):
    def __str__(self):
        return f"[Titulado] {super().__str__()}"

class AlumnoRegular(Alumno, EstudianteBehavior):
    def estudiar(self) -> str:
        return f"{self.nombre} está estudiando"
    
    def __str__(self):
        return f"[Regular] {super().__str__()}"

class AlumnoAyudante(AlumnoRegular, AyudanteBehavior):
    def hacer_ayudantia(self) -> str:
        return f"{self.nombre} está haciendo una ayudantía"
    
    def __str__(self):
        return f"[Ayudante] {super().__str__()}"

class AlumnoMagister(AlumnoRegular, ProfesorBehavior):
    def hacer_clases(self) -> str:
        return f"{self.nombre} está dando clases en el magister"
    
    def __str__(self):
        return f"[Magister] {super().__str__()}"

class AlumnoDoctorado(AlumnoMagister, InvestigadorBehavior):
    def investigar(self) -> str:
        return f"{self.nombre} está investigando para su doctorado"
    
    def __str__(self):
        return f"[Doctorado] {super().__str__()}"