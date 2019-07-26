from django import forms
from .models import Curriculo

class MostraCurriculo(forms.ModelForm):

	name = forms.CharField(
		widget=forms.TextInput(attrs={
			'readonly':'True',
			'size':'30'
			})
		)
	description = forms.CharField(
		widget=forms.TextInput(attrs={
			'readonly':'True',
			'size':'40'
			})
		) 

	start_date = forms.CharField(
		widget=forms.TextInput(attrs={
			'readonly':'True',
			'size':'10'
			})
		)

	class Meta:
		model = Curriculo
		fields = ['name','description','start_date']
	
