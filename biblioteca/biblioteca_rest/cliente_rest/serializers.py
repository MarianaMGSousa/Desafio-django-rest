from dataclasses import fields
from rest_framework import serializers
from .models import Cliente #importa a model pq vai ser como os dados de lá vão se comportar

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nome', 'idade', 'rg', 'cpf', 'email', 'telefone')
