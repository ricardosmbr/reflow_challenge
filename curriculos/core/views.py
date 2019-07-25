from django.shortcuts import render, redirect, get_object_or_404
from .models import Curriculo
from django.contrib.auth.decorators import login_required


def home(request):
	return render(request,'base.html')

@login_required
def lista(request):
	curriculo = Curriculo.objects.all()
	pesquisa =''
	if request.method == 'POST':
		pesquisa = request.POST.get("pescli")
		curriculo = Curriculo.objects.filter(name__icontains=pesquisa)
	template_name = 'lista.html'
	context = {
		'curriculo':curriculo
	}
	return render(request,template_name,context)

