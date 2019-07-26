from django.shortcuts import render, redirect, get_object_or_404
from .models import Curriculo
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import MostraCurriculo,NovoCurriculo
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

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

@login_required
def mostra(request,pk):
	template_name = 'mostra.html'
	curriculo = Curriculo.objects.get(pk=pk)
	arquivo = settings.MEDIA_URL + curriculo.image.name
	nome_arq = curriculo.image.name
	context = {}
	form = MostraCurriculo(instance=curriculo)
	if request.method == 'POST':
		return redirect('lista')
	context['form'] = form
	context['arquivo'] = arquivo
	context['nome_arq'] = nome_arq
	return render(request, template_name, context)

@login_required
def novo(request):
	context = {}
	template_name = 'novo.html'
	if request.method == 'POST':
		form = NovoCurriculo(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,"Curriculo cadastrado com sucesso")
			return redirect('lista')
	else:
		form = NovoCurriculo()	
	context['form'] = form
	return render(request, template_name, context)

	
