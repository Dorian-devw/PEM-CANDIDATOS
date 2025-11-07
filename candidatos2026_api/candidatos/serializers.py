from rest_framework import serializers
from .models import Candidato, Proyecto, Denuncia

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'

class DenunciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Denuncia
        fields = '__all__'

class CandidatoSerializer(serializers.ModelSerializer):
    proyectos = ProyectoSerializer(many=True, read_only=True)
    denuncias = DenunciaSerializer(many=True, read_only=True)

    class Meta:
        model = Candidato
        fields = '__all__'
