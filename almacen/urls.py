from django.conf.urls import url
from .views import Agregar, Comprar, Salir, Stock, Lcompra, Lsalida

urlpatterns = [
	url(r'^$', Stock.as_view(), name='stock'),
    url(r'^agregar/$', Agregar.as_view(), name='agregar'),
    url(r'^comprar/(?P<pk>\d+)', Comprar.as_view(), name='comprar'),
    url(r'^salida/(?P<pk>\d+)', Salir.as_view(), name='salida'),
    url(r'^compras/$', Lcompra.as_view(), name='lcompra'),
    url(r'^salidas/$', Lsalida.as_view(), name='lsalida'),
]