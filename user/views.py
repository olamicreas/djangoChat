from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    user = User.objects.all()
    return render(request, 'user/home.html', {'user': user})

def register(request):
    form = RegForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.data.get('username')
            messages.success(request, f'Account created successfully for {username}' )
            return redirect('login')

    return render(request, 'user/register.html', {'form': form})