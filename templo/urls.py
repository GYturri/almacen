from django.conf.urls import url, include
from django.contrib import admin
from .views import Home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^almacen/', include('almacen.urls', namespace="almacen")),
]
