from rest_framework import serializers
from apps.core.models import Mag, User, Prod

class MagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Mag

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User

class ProdSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Prod
