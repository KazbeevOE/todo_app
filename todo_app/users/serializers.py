from rest_framework import serializers

from .models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'organizations', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class UserAuthenticateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
