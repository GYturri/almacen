from django.db import models

class OtroGasto(models.Model):
	nombre = models.CharField(max_length=150)
	costo = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	fecha = models.DateField('registro', auto_now_add=True)
	def __str__(self):
		return '%s %s' % (self.nombre, self.costo)

class OtraVenta(models.Model):
	nombre = models.CharField(max_length=150)
	costo = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	fecha = models.DateField('registro', auto_now_add=True)
	def __str__(self):
		return '%s %s' % (self.nombre, self.costo)

class Gasto(models.Model):
	costo = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	fecha = models.DateField('registro', auto_now_add=True, unique_for_date="fecha")
	def __str__(self):
		return str(self.costo)

class Venta(models.Model):
	costo = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	fecha = models.DateField('registro', auto_now_add=True, unique_for_date="fecha")
	def __str__(self):
		return str(self.costo)