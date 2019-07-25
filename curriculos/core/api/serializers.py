from rest_framework import serializers
from core.models import Curriculo

class CurriculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculo
        fields = ('name', 'description', 'start_date','image','create_at','update_at')