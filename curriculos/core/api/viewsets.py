from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from core.models import Curriculo
from .serializers import CurriculoSerializer

class CurriculoViewSet(viewsets.ModelViewSet):
    queryset = Curriculo.objects.all()
    serializer_class = CurriculoSerializer
