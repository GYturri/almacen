# -*- coding: utf-8 -*-
from django import forms
from .models import Producto

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
	class Meta:
		model = Producto
		exclude = ("id","stock",)
