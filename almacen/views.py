from django.views.generic import CreateView, TemplateView, ListView
from django.http import HttpResponseRedirect
from .models import Producto, Compra, Salida
from .forms import NProducto, NCompra

class Agregar(CreateView):
	template_name = "almacen/agregar.html"
	model = Producto
	form_class = NProducto
	success_url = '/'
	def form_valid(self, form):
		return super(Agregar, self).form_valid(form)
	def form_invalid(self, form):
		return super(Agregar, self).form_invalid(form)

class Comprar(TemplateView):
	template_name = "almacen/comprar.html"
	def get_context_data(self, **kwargs):
		context = super(Comprar, self).get_context_data(**kwargs)
		context['productos'] = Producto.objects.all()
		return context
	def post(self, request, *args, **kwargs):
		ncompra = Compra()
		producto = Producto.objects.get(id=request.POST['producto'])
		producto.stock = producto.stock + int(request.POST['cantidad'])
		producto.save()
		ncompra.producto = producto
		ncompra.cantidad = request.POST['cantidad']
		ncompra.costo = request.POST['precio']
		ncompra.save()
		return HttpResponseRedirect('/')

class Salir(TemplateView):
	template_name = "almacen/salida.html"
	def get_context_data(self, **kwargs):
		context = super(Salir, self).get_context_data(**kwargs)
		context['productos'] = Producto.objects.all()
		return context
	def post(self, request, *args, **kwargs):
		nsalida = Salida()
		producto = Producto.objects.get(id=request.POST['producto'])
		producto.stock = producto.stock - int(request.POST['cantidad'])
		producto.save()
		nsalida.producto = producto
		nsalida.cantidad = request.POST['cantidad']
		nsalida.save()
		return HttpResponseRedirect('/')

class Stock(ListView):
	template_name = "almacen/stock.html"
	model = Producto
	context_object_name = 'productos'
