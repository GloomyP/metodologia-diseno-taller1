class Asignatura:
    def __init__(self, nombre: str, codigo: str, creditos: int, nivel: str = "pregrado"):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.nivel = nivel  # pregrado, magister, doctorado
    
    def __str__(self):
        return f"{self.nombre} ({self.codigo}) - {self.creditos} créditos - Nivel: {self.nivel}"
    
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'codigo': self.codigo,
            'creditos': self.creditos,
            'nivel': self.nivel
        }