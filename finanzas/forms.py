# -*- coding: utf-8 -*-
from django import forms
from .models import Gasto, Venta, OtroGasto, OtraVenta

class NGastoD(forms.ModelForm):
	costo = forms.CharField(widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Gasto del dia',
			'type': 'number',
			'required': '',
		}))
	class Meta:
		model = Gasto
		exclude = ("id",)

class NVentaD(forms.ModelForm):
	costo = forms.CharField(widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Venta del dia',
			'type': 'number',
			'required': '',
		}))
	class Meta:
		model = Venta
		exclude = ("id",)

class NOGasto(forms.ModelForm):
	nombre = forms.CharField(widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Detalle',
			'required': '',
		}))
	costo = forms.CharField(widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Precio',
			'type': 'number',
			'required': '',
		}))
	class Meta:
		model = OtroGasto
		exclude = ("id",)

class NOVenta(forms.ModelForm):
	nombre = forms.CharField(widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Detalle',
			'required': '',
		}))
	costo = forms.CharField(widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Precio',
			'type': 'number',
			'required': '',
		}))
	class Meta:
		model = OtraVenta
		exclude = ("id",)