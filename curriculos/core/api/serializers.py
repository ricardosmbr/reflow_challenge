from rest_framework import serializers
from core.models import Curriculo

class CurriculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculo
        fields = ('id','name', 'description','image','create_at','update_at')