from django.shortcuts import render
from .models import Curriculo

def home(request):
	return render(request,'base.html')

