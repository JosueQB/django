from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    Cedula= models.CharField(max_length=10,unique=True,null=True,blank=True)
    telefono = models.CharField(max_length=10,unique=True,null=True,blank=True)
    Fecha_nac = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=200)
    email = models.EmailField(unique=True,null=False,blank=False)
    peso = models.CharField(max_length=3)
    Genero = models.BooleanField('masculino',default=True, null=True, blank=True)
    Estatura = models.CharField(max_length=3)

    def _str_(self):
        return f"{self.nombre} {self.apellido}"