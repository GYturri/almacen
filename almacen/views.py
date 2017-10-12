from django.views.generic import CreateView
from .models import Producto
from .forms import NProducto

class Agregar(CreateView):
	template_name = "almacen/agregar.html"
	model = Producto
	form_class = NProducto
	success_url = '/'
	def form_valid(self, form):
		return super(Agregar, self).form_valid(form)
	def form_invalid(self, form):
		return super(Agregar, self).form_invalid(form)