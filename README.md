# Desafio-django-rest

![image](https://user-images.githubusercontent.com/92062708/178159018-76bcc1be-64d2-49ed-883d-eb18c2a732f1.png)
![image](https://user-images.githubusercontent.com/92062708/178159033-10322c47-b13b-44cd-adf8-a2cfe28fcf02.png)


PASSO – A – PASSO DA REALIZAÇÃO

1 - Criei um ambiente virtual biblioteca

2 - Ativei o ambiente virtual

3 - Instalei o django

4 - Criei um projeto biblioteca_rest

5 - Criei um aplicativo cliente_rest para salvar os dados de clientes

6 - Instalei as dependências do djangorestframework, que são:

  pip install 
  
  pip install markdown
  
  pip install django-filter
  
7 - Registrei o django rest e o aplicativo no settings.py
  
8 - Crie no models.py um tabela no banco chamada Cliente com os seguintes atributos: nome, idade, RG, CPF, E-mail e telefone

9 - Instalei pip install django-phonenumber-field[phonenumberslite] para o atributo telefone da tabela

10 - Registrei settings.py 'phonenumber_field', na lista de aplicativos instalados

11 - Instalei pip install django-cpf e registrei no settings na lista de aplicativos

12 - Dei o makemigrations e o migrate

13 - Crie um super usuário com o comando:

  python manage.py createsuperuser
  
14 - Registrei a tabela Cliente no admin.py

15 - Criei um novo arquivo dentro do aplicativo chamado serializers.py para fazer a serialização e apresentar os dados em json

16 - Na views.py importei e criei o queryset para ter a lista com todos os clientes a partir da base de dados

17 - Na urls.py do projeto criei a rota

18 - Rodei o runserver e apareceu essa tela:

![image](https://user-images.githubusercontent.com/92062708/178159301-286145a9-a624-4a16-9d36-5af29e01f789.png)

19 – Para criar o cache no views.py, importei o cache_page e o method_decorator depois criei a função list que já vem pronta do Viewsets 

20 – Para criar os testes eu exclui o arquivo que já vem pronto do aplicativo e lá criei uma pasta chamada tests. Dentro dessa pasta eu criei um módulo inicial __init__.py e o arquivo que vou testar chamado test_models.py

21 – Fazendo teste com unittest

  •	Testei se o atributo idade 38 se era igual a 40 e deu erro
  ![image](https://user-images.githubusercontent.com/92062708/178159340-781420fe-9383-4352-beb8-cec5c763bb36.png)
  
  •	Testei se o atributo idade 38 era igual a 38 e deu certo
  ![image](https://user-images.githubusercontent.com/92062708/178159352-ff4a9bfe-a275-4d3f-998d-1b3070769c76.png)

22 – Fazendo teste de usabilidade exploratório

  •	Entrei na API
  
  ![image](https://user-images.githubusercontent.com/92062708/178159405-6d5cd06b-8674-43a8-a1c9-e41a54526277.png)
  
  •	Cliquei no botão GET pata explorar se estava funcionando como esperado
  ![image](https://user-images.githubusercontent.com/92062708/178159417-fb431564-bc3c-46ed-a3b6-4df1d11aa785.png)
  
  •	Cliquei em json e foi gerado o arquivo neste formato
  ![image](https://user-images.githubusercontent.com/92062708/178159432-c0d9d667-3112-496c-b0b7-fc53a49c0173.png)

  
