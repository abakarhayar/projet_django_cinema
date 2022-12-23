from django.http import HttpResponse
from django.template import loader
from .models import Cinema
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages



def index(request):
    
    cinema = Cinema.objects.all()
    return render(request,'tp/index.html', context={"cinemas":cinema})
def catalogue(request):
    
    cinema = Cinema.objects.all()
    return render(request,'tp/catalogue.html', context={"cinemas":cinema})

def cinema_detail(request, id):
    cinema = get_object_or_404(Cinema, id=id)
    return render(request,'tp/detail.html', context={"cinema":cinema})

def register(request):
	if request.method == 'POST' :
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()		
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request,user)	
			messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')					
			return redirect('index')
	else :
		form = UserCreationForm()
	return render(request,'tp/register.html',{'form' : form}) 