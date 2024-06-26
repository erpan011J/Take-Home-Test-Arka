from rest_framework import serializers
from .models import User, Product, Client


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'name', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'name', 'description', 'price']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['client_id', 'user', 'start_date', 'contract_value']
