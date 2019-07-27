## Gestor de Curriculo 1.0

Originalemnte feito na plataforma Linux Debian 9.3

Pré-requisitos
Python 3.7

#criando ambiente para a aplicação
python -m venv venv 

#ativando o ambiente
. venv/bin/activate

#instalando dependências
pip install -r requirements.txt

#configurando a aplicação dentro da pasta curriculos  
python manage.py makemigrations
python manage.py migrate

#criando usuario para a aplicação
python manage.py createsuperuser

#rodando a aplicação OBS: sempre ativar o ambiente antes
python manage.py runserver

#testando a aplicação
http://localhost:8000

#consumindo a API

http://localhost:8000/api