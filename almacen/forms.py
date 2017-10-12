# -*- coding: utf-8 -*-
from django import forms
from .models import Producto, Compra

class NProducto(forms.ModelForm):
	nombre = forms.CharField(widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Nombre',
			'required': '',
		}))
	detalle = forms.CharField(widget=forms.Textarea(attrs={
			'class': 'form-control',
			'rows':'2',
			'placeholder': 'Detalle',
			'required': '',
		}))
	stock = forms.CharField(widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Cantidad',
			'type': 'number',
			'required': '',
		}))
	class Meta:
		model = Producto
		exclude = ("id",)

class NCompra(forms.ModelForm):
	producto = forms.CharField(widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Nombre',
			'required': '',
		}))
	cantidad = forms.CharField(widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Cantidad',
			'type': 'number',
			'required': '',
		}))
	class Meta:
		model = Compra
		exclude = ("id",)
