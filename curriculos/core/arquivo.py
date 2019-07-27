import os 
from django.conf import settings

def Apaga(con):

	caminho = settings.BASE_DIR + '/curriculos/media/'
	arquivo = str(con.image)
	
	dir = os.listdir(caminho)

	for file in dir:
		if file == arquivo:
			os.remove(caminho + '/'+ file)
	
