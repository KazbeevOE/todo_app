from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ('id', 'email', 'first_name', 'last_name',
                 'organizations', 'password')
        extra_kwargs = {'password': {'write_only': True}}
