import unittest
     
class TestCliente(unittest.TestCase):
    def test_idade(self):
        idade= 38
        self.assertEquals(38, idade)
        
if __name__ == "__name__":
    unittest.main()
#testa com o comando python -m unittest
        





# from django.test import TestCase
# from cliente_rest.models import Cliente

# class ClienteTestCase(TestCase):
#     def setup(self): #criação do objeto para saber se ele estar ou não no banco de dados para teste, esse valor nãoserácriado no banco de dados principal
#         Cliente.objects.create(
#             nome=Mariana 
#         )      
        
#     def test_return_str(self):
#         p1=Cliente.objects.get(nome=Mariana)
#         self.assertEquals(p1.__str__(), Mariana)
       