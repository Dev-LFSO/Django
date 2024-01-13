from django.contrib import admin

# Register your models here.
from .models import Sala, Topico, Mensagem

admin.site.register(Sala)
admin.site.register(Topico)
admin.site.register(Mensagem)