from django.db import models
from  phonenumber_field.modelfields  import  PhoneNumberField
from cpf_field.models import CPFField

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    rg = models.CharField(max_length=11)
    cpf = CPFField('cpf')
    email = models.EmailField()
    telefone = PhoneNumberField ()
    
    def __str__(self):
        return self.nome