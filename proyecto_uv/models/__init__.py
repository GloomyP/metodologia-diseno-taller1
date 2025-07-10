# Exporta las clases importantes para facilitar los imports
from .alumno import Alumno, AlumnoTitulado, AlumnoRegular, AlumnoAyudante, AlumnoMagister, AlumnoDoctorado
from .asignatura import Asignatura
from .interfaces import EstudianteBehavior, AyudanteBehavior, ProfesorBehavior, InvestigadorBehavior, NotasBehavior

__all__ = [
    'Alumno', 'AlumnoTitulado', 'AlumnoRegular', 'AlumnoAyudante', 
    'AlumnoMagister', 'AlumnoDoctorado', 'Asignatura',
    'EstudianteBehavior', 'AyudanteBehavior', 'ProfesorBehavior', 
    'InvestigadorBehavior', 'NotasBehavior'
]