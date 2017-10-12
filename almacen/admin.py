from django.contrib import admin
from .models import Producto, Compra, Salida

admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(Salida)