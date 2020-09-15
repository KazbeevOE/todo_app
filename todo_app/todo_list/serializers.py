from rest_framework import serializers

from .models import Board, Task


class BoardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class BoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['name', 'description']


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description']


class TaskChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'board']


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name']
