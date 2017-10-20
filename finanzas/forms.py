# -*- coding: utf-8 -*-
from django import forms
from .models import Gasto, Venta, OtroGasto, OtraVenta

class NGastoD(forms.ModelForm):
	costo = forms.CharField(widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': '00.00',
			'type': 'number',
			'step': '0.1',
			'required': '',
		}))
	class Meta:
		model = Gasto
		exclude = ("id",)

class NVentaD(forms.ModelForm):
	costo = forms.CharField(widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': '00.00',
			'type': 'number',
			'step': '0.1',
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
			'placeholder': '00.00',
			'type': 'number',
			'step': '0.1',
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
			'placeholder': '00.00',
			'type': 'number',
			'step': '0.1',
			'required': '',
		}))
	class Meta:
		model = OtraVenta
		exclude = ("id",)