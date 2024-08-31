from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=8)
    fecha_de_nacimiento = models.DateField()
    email = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre} - DNI: {self.dni}"
    
class Materia(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    turno_de_cursada = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True, null=True)
    ofertada = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nombre
    
class Solicitud(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        ACEPTADA = 'ACEPTADA', 'Aceptada'
        RECHAZADA = 'RECHAZADA', 'Rechazada'

    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    fecha_de_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PENDIENTE)

    def __str__(self) -> str:
        return f"Solicitud de {self.estudiante.apellido}, {self.estudiante.nombre} para inscribirse a {self.materia.nombre}"

