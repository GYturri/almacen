from django.conf.urls import url
from .views import GastoD, VentaD, OGasto, OVenta, DelMes

urlpatterns = [
	#url(r'^$', Stock.as_view(), name='stock'),
    url(r'^gasto/$', GastoD.as_view(), name='gasto'),
    url(r'^venta/$', VentaD.as_view(), name='venta'),
    url(r'^otro_gasto/$', OGasto.as_view(), name='ogasto'),
    url(r'^otra_venta/$', OVenta.as_view(), name='oventa'),
    url(r'^delmes/$', DelMes.as_view(), name='delmes'),
]