from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseNotAllowed
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    elif request.method == "GET":
        form = UserCreationForm()
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
    
    return render(request,'authentication/register.html', {'form':form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            return redirect('home')
    elif request.method == 'GET':
        form = AuthenticationForm()
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
    
    return render(request,'authentication/login.html', {'form':form})
