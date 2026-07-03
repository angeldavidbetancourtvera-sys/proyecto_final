from django.db import models
from django.contrib.auth.models import User

# MODELO 1: PARA LOS PROYECTOS
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField()  
    
    # El creador es el usuario que inició el proyecto, en otras palabras, el autor del proyecto. Esto permite que cada proyecto esté asociado a un usuario específico.
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre


# MODELO 2: PARA LAS TAREAS DE CADA PROYECTO
class Tarea(models.Model):
    # Opciones de estado para las tareas
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('PROCESO', 'En Proceso'),
        ('FINALIZADO', 'Finalizado'),
    ]

    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_limite = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    
    # Vinculamos la tarea a un proyecto específico
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo