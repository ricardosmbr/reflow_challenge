from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from core.models import Curriculo
from .serializers import CurriculoSerializer
from core.arquivo import Apaga
from rest_framework.permissions import IsAuthenticated

class CurriculoViewSet(viewsets.ModelViewSet):
    
    serializer_class = CurriculoSerializer

    def get_queryset(self):
    	return Curriculo.objects.all()

    
    def destroy(self,request,*args,**kargs):
    	pk= kargs['pk']
    	curriculo = Curriculo.objects.get(pk=pk)
    	Apaga(curriculo)
    	return super(CurriculoViewSet,self).destroy(request,*args,**kargs)
  