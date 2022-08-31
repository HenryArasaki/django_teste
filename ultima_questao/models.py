from django.db import models

# Create your models here.

class Time(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome


class Jogador(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField ()
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
