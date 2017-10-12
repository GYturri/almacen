from django.conf.urls import url
from .views import Agregar, Comprar, Salir, Stock

urlpatterns = [
	url(r'^$', Stock.as_view(), name='stock'),
    url(r'^agregar/$', Agregar.as_view(), name='agregar'),
    url(r'^comprar/$', Comprar.as_view(), name='comprar'),
    url(r'^salida/$', Salir.as_view(), name='salida'),
]