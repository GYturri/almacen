from django.conf.urls import url
from .views import GastoD, VentaD, OGasto, OVenta, DelMes, LgastosD, ELgastoD, LventasD, LAventaD, LOVenta, EOventa, LOGasto, EOGasto

urlpatterns = [
	#url(r'^$', Stock.as_view(), name='stock'),
    url(r'^gasto/$', GastoD.as_view(), name='gasto'),
    url(r'^venta/$', VentaD.as_view(), name='venta'),
    url(r'^otro_gasto/$', OGasto.as_view(), name='ogasto'),
    url(r'^otra_venta/$', OVenta.as_view(), name='oventa'),
    url(r'^delmes/$', DelMes.as_view(), name='delmes'),
    url(r'^gastos/$', LgastosD.as_view(), name='lgastosd'),
    url(r'^gastos/(?P<pk>\d+)', ELgastoD.as_view(), name='elgastod'),
    url(r'^ventas/$', LventasD.as_view(), name='lventasd'),
    url(r'^venta/(?P<pk>\d+)', LAventaD.as_view(), name='laventad'),
    url(r'^otros_gastos/$', LOGasto.as_view(), name='logastos'),
    url(r'^o_gasto/(?P<pk>\d+)', EOGasto.as_view(), name='eogasto'),
    url(r'^otras_ventas/$', LOVenta.as_view(), name='loventas'),
    url(r'^o_gasto/(?P<pk>\d+)', EOventa.as_view(), name='eoventa'),
]