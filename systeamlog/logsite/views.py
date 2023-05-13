from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
 
    
    return render(request, 'home.html')


def registrare(request):
    if request.method=='POST':
        username        = request.POST['utiliator']
        email           = request.POST['email'] 
        password        = request.POST['password']
        verify_password = request.POST['confirm-password'] 
        if User.objects.filter(username = username).first():
            messages.error(request, 'Ai introdus un nume existent la noi pe platforma')
            return redirect('registrare-url')
        elif User.objects.filter(email = email).first():
            messages.error(request, 'Ai introdus un email existent la noi pe platforma')
            return redirect('registrare-url')
        elif password != verify_password:
            messages.error(request, 'Introduceti parola la fel in ambele casute pentru a continua..')
            
            print('Parola nu se aseamana')
        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        return redirect('logins-url')
    return render(request, 'register.html')

def logare(request):
    if request.method=='POST':
        username = request.POST['utiliator']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('logins-url')
            
    return render(request, 'log.html')
@login_required
def logut(request):
    logout(request)
    return redirect('logins-url')

def msg(request):
    return render(request, 'message.html')



