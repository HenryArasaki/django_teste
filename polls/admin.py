from django.contrib import admin

from polls.models import Choice, Equipamento, Question, Cidade


@admin.action(description="Trocar nome")
def action_trocar_nome(modelAdmin,request,queryset):
    for equipamento in queryset:
        equipamento.nome = 'Nome trocado'
        equipamento.save()


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    

admin.site.register(Question, QuestionAdmin)


class EquipamentoAdmin(admin.ModelAdmin):
    fields = ['nome','ip','cidade']
    list_display = ('nome','ip','cidade','numero_de_caracteres_do_ip')
    search_fields = ['ip','nome','cidade__nome']
    list_filter = ['cidade']
    autocomplete_fields = ['cidade']
    actions = [action_trocar_nome]
    def save_model(self, request, obj, form, change):
        print('OK')
        super().save_model(request, obj, form, change)
    
    
admin.site.register(Equipamento, EquipamentoAdmin)


class EquipamentoInline(admin.TabularInline):
    model = Equipamento
    extra = 1


class CidadeAdmin(admin.ModelAdmin):
    fields = ['nome']
    search_fields = ['nome']
    inlines = [EquipamentoInline]

    
    
admin.site.register(Cidade, CidadeAdmin)