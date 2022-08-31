from django.contrib import admin

from ultima_questao.models import Jogador, Time


class JogadorAdmin(admin.ModelAdmin):
    fields = ['nome', 'idade','time']
    list_display = ('nome','idade','time')

admin.site.register(Jogador, JogadorAdmin)

class TimeAdmin(admin.ModelAdmin):
    fields = ['nome']

admin.site.register(Time, TimeAdmin)