from django.conf.urls import url
from .views import Agregar

urlpatterns = [
    url(r'^agregar/$', Agregar.as_view(), name='agregar'),
    #url(r'^nuevo-paciente/$', Npaciente.as_view(), name='npaciente'),
    #url(r'^buscar/$', Buscar.as_view(), name='buscar'),
]