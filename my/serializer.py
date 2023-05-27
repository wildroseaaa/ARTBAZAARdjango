from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User1
        fields=('id','email','number')



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

        def create(self,validated_data):
            img = validated_data['img']
            body = validated_data['body']
            product = Product.objects.create(**validated_data)
