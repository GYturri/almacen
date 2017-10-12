from django.views.generic import CreateView, TemplateView, ListView
from django.http import HttpResponseRedirect
from .models import Gasto, Venta, OtroGasto, OtraVenta
from .forms import NGastoD, NVentaD, NOGasto, NOVenta
from almacen.models import Compra

class GastoD(CreateView):
	template_name = "finanzas/ngasto.html"
	model = Gasto
	form_class = NGastoD
	success_url = '/'
	def form_valid(self, form):
		return super(GastoD, self).form_valid(form)
	def form_invalid(self, form):
		return super(GastoD, self).form_invalid(form)

class VentaD(CreateView):
	template_name = "finanzas/nventa.html"
	model = Venta
	form_class = NVentaD
	success_url = '/'
	def form_valid(self, form):
		return super(VentaD, self).form_valid(form)
	def form_invalid(self, form):
		return super(VentaD, self).form_invalid(form)

class OGasto(CreateView):
	template_name = "finanzas/ogasto.html"
	model = OtroGasto
	form_class = NOGasto
	success_url = '/'
	def form_valid(self, form):
		return super(OGasto, self).form_valid(form)
	def form_invalid(self, form):
		return super(OGasto, self).form_invalid(form)

class OVenta(CreateView):
	template_name = "finanzas/oventa.html"
	model = OtraVenta
	form_class = NOVenta
	success_url = '/'
	def form_valid(self, form):
		return super(OVenta, self).form_valid(form)
	def form_invalid(self, form):
		return super(OVenta, self).form_invalid(form)

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