from django.contrib import admin

# Register your models here.

from gestionAlmuerzos.models import Nora,Menu,Calendario,Empleado,Pedido

admin.site.register(Nora)
admin.site.register(Menu)
admin.site.register(Calendario)
admin.site.register(Empleado)
admin.site.register(Pedido)




