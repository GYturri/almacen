from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.http import HttpResponseRedirect
from .models import Gasto, Venta, OtroGasto, OtraVenta
from .forms import NGastoD, NVentaD, NOGasto, NOVenta
from almacen.models import Compra

class GastoD(CreateView):
	template_name = "finanzas/ngasto.html"
	model = Gasto
	form_class = NGastoD
	success_url = '/finanzas/gastos/'
	def form_valid(self, form):
		return super(GastoD, self).form_valid(form)
	def form_invalid(self, form):
		return super(GastoD, self).form_invalid(form)

class VentaD(CreateView):
	template_name = "finanzas/nventa.html"
	model = Venta
	form_class = NVentaD
	success_url = '/finanzas/ventas/'
	def form_valid(self, form):
		return super(VentaD, self).form_valid(form)
	def form_invalid(self, form):
		return super(VentaD, self).form_invalid(form)

class OGasto(CreateView):
	template_name = "finanzas/ogasto.html"
	model = OtroGasto
	form_class = NOGasto
	success_url = '/finanzas/otros_gastos/'
	def form_valid(self, form):
		return super(OGasto, self).form_valid(form)
	def form_invalid(self, form):
		return super(OGasto, self).form_invalid(form)

class OVenta(CreateView):
	template_name = "finanzas/oventa.html"
	model = OtraVenta
	form_class = NOVenta
	success_url = '/finanzas/otras_ventas/'
	def form_valid(self, form):
		return super(OVenta, self).form_valid(form)
	def form_invalid(self, form):
		return super(OVenta, self).form_invalid(form)

class LgastosD(ListView):
	template_name = "finanzas/lgastosd.html"
	model = Gasto
	context_object_name = 'gastos'

class ELgastoD(DetailView):
	template_name = "finanzas/elgastod.html"
	model = Gasto
	slug_field = 'id'
	context_object_name = 'gasto'
	def post(self, request, *args, **kwargs):
		gastod = Gasto.objects.get(id=self.kwargs['pk'])
		gastod.fecha = request.POST['fecha']
		gastod.costo = request.POST['costo']
		gastod.save()
		return HttpResponseRedirect('/finanzas/gastos/')

class LventasD(ListView):
	template_name = "finanzas/lventasd.html"
	model = Venta
	context_object_name = 'ventas'

class LAventaD(DetailView):
	template_name = "finanzas/laventad.html"
	model = Venta
	slug_field = 'id'
	context_object_name = 'venta'
	def post(self, request, *args, **kwargs):
		ventad = Venta.objects.get(id=self.kwargs['pk'])
		ventad.fecha = request.POST['fecha']
		ventad.costo = request.POST['costo']
		ventad.save()
		return HttpResponseRedirect('/finanzas/ventas/')

class LOVenta(ListView):
	template_name = "finanzas/loventas.html"
	model = OtraVenta
	context_object_name = 'ventas'

class EOventa(DetailView):
	template_name = "finanzas/laoventa.html"
	model = OtraVenta
	slug_field = 'id'
	context_object_name = 'venta'
	def post(self, request, *args, **kwargs):
		oventa = OtraVenta.objects.get(id=self.kwargs['pk'])
		oventa.nombre = request.POST['nombre']
		oventa.fecha = request.POST['fecha']
		oventa.costo = request.POST['costo']
		oventa.save()
		return HttpResponseRedirect('/finanzas/otras_ventas/')

class LOGasto(ListView):
	template_name = "finanzas/logastos.html"
	model = OtroGasto
	context_object_name = 'gastos'

class EOGasto(DetailView):
	template_name = "finanzas/elogasto.html"
	model = OtroGasto
	slug_field = 'id'
	context_object_name = 'gasto'
	def post(self, request, *args, **kwargs):
		ogasto = OtroGasto.objects.get(id=self.kwargs['pk'])
		ogasto.nombre = request.POST['nombre']
		ogasto.fecha = request.POST['fecha']
		ogasto.costo = request.POST['costo']
		ogasto.save()
		return HttpResponseRedirect('/finanzas/otros_gastos/')

class DelMes(TemplateView):
	template_name = "finanzas/delmes.html"
	def get_context_data(self, **kwargs):
		context = super(DelMes, self).get_context_data(**kwargs)
		compras = Compra.objects.all()
		precompras = 0
		for x in compras:
			precompras = precompras + x.costo
		context['compras'] = precompras
		gastod = Gasto.objects.all()
		pregastod = 0
		for y in gastod:
			pregastod = pregastod + y.costo
		context['gastod'] = pregastod
		ventad = Venta.objects.all()
		preventad = 0
		for y in ventad:
			preventad = preventad + y.costo
		context['ventad'] = preventad
		ogasto = OtroGasto.objects.all()
		preogasto = 0
		for y in ogasto:
			preogasto = preogasto + y.costo
		context['ogasto'] = preogasto
		oventa = OtraVenta.objects.all()
		preoventa = 0
		for y in oventa:
			preoventa = preoventa + y.costo
		context['oventa'] = preoventa
		context['total'] = (preventad+preoventa)-(precompras+pregastod+preogasto)
		return context