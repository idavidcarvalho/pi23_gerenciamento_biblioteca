from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def perfil(request):
    return render(request, 'perfil.html')

def autenticar(request):
    if request.POST:
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect ('perfil')
        else:
            return render(request, 'registration\login.html')
    else:
        return render(request, 'registration\login.html')

def desconectar(request):
    logout(request)
    return redirect('login')
