from django.db import models

class Producto(models.Model):
	nombre = models.CharField(max_length=50, unique=True)
	detalle = models.CharField(max_length=200)
	stock = models.PositiveIntegerField(default=0)
	def __str__(self):
		return '%s %s' % (self.nombre, self.detalle)

class Compra(models.Model):
	producto = models.ForeignKey(Producto)
	cantidad = models.PositiveIntegerField(default=0)
	costo = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	fecha = models.DateField('registro', auto_now_add=False)
	def __str__(self):
		return self.producto.nombre

class Salida(models.Model):
	producto = models.ForeignKey(Producto)
	cantidad = models.PositiveIntegerField(default=0)
	fecha = models.DateField('registro', auto_now_add=True)
	def __str__(self):
		return self.producto.nombre