import datetime

from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

def valid_ip(ip):
    if ip == "1.1.1.1":
        raise ValidationError(str(ip) + " é um IP inválido")

class Equipamento(models.Model):
    nome = models.CharField(max_length=50)
    ip = models.GenericIPAddressField(validators=[valid_ip])
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
    def numero_de_caracteres_do_ip(self):
        tamanho = len(self.ip) - 3
        return tamanho
