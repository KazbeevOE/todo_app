from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=64, verbose_name='Organization name')
    description = models.CharField(max_length=256, verbose_name='Organization description')


class Board(models.Model):
    name = models.CharField(max_length=64, verbose_name='Board name')
    description = models.CharField(max_length=256, verbose_name='Board description')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return f'Organization: {self.organization.name}, Name: {self.name}'


class Task(models.Model):
    name = models.CharField(max_length=64, verbose_name='Task name')
    description = models.CharField(max_length=256, verbose_name='Task description')
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
