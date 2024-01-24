from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Test_model        # product 모델 사용
        fields = '__all__'