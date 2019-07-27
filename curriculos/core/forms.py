from django import forms
from .models import Curriculo
import datetime

class MostraCurriculo(forms.ModelForm):

	name = forms.CharField(widget=forms.TextInput(attrs={
			'readonly':'True',
			'size':'30'
			}))
	description = forms.CharField(widget=forms.TextInput(attrs={
			'readonly':'True',
			'size':'40'
			})) 

	class Meta:
		model = Curriculo
		fields = ['name','description']
	
class NovoCurriculo(forms.ModelForm):

	class Meta:
		model = Curriculo
		fields = ['name','description','image']

class EditarCurriculo(forms.ModelForm):
	
	class Meta:
		model = Curriculo
		fields = ['name','description','image']