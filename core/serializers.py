from rest_framework import serializers
from core.models import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields =('id', 'nombre', 'apellido', 'Cedula', 'telefono', 'Fecha_nac', 'direccion', 'email', 'peso', 'Genero', 'Estatura')

        read_only_fields = ('id',)