from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.http import HttpResponseRedirect
from .models import Producto, Compra, Salida
from .forms import NProducto

class Agregar(CreateView):
	template_name = "almacen/agregar.html"
	model = Producto
	form_class = NProducto
	success_url = '/almacen/'
	def form_valid(self, form):
		return super(Agregar, self).form_valid(form)
	def form_invalid(self, form):
		return super(Agregar, self).form_invalid(form)

class Comprar(DetailView):
	template_name = "almacen/comprar.html"
	model = Producto
	slug_field = 'id'
	context_object_name = 'producto'
	def post(self, request, *args, **kwargs):
		producto = Producto.objects.get(id=self.kwargs['pk'])
		producto.stock = producto.stock + int(request.POST['cantidad'])
		producto.save()
		ncompra = Compra()
		ncompra.producto = producto
		ncompra.cantidad = request.POST['cantidad']
		ncompra.costo = request.POST['precio']
		ncompra.save()
		return HttpResponseRedirect('/almacen/')

class Salir(DetailView):
	template_name = "almacen/salida.html"
	model = Producto
	slug_field = 'id'
	context_object_name = 'producto'
	def post(self, request, *args, **kwargs):
		producto = Producto.objects.get(id=self.kwargs['pk'])
		producto.stock = producto.stock - int(request.POST['cantidad'])
		producto.save()
		nsalida = Salida()
		nsalida.producto = producto
		nsalida.cantidad = request.POST['cantidad']
		nsalida.save()
		return HttpResponseRedirect('/almacen/')

class Stock(ListView):
	template_name = "almacen/stock.html"
	model = Producto
	context_object_name = 'productos'

class Lcompra(ListView):
	template_name = "almacen/lcompras.html"
	model = Compra
	context_object_name = 'compras'

class Lsalida(ListView):
	template_name = "almacen/lsalidas.html"
	model = Salida
	context_object_name = 'salidas'
