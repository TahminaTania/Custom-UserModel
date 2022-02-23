# from multiprocessing import context
from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import Sregistration, Uregistration
from .models import subscriber,profiles
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def RegForm(request):
    form = Uregistration()
    if request.method == 'POST':
        form = Uregistration(request.POST)
        if form.is_valid():
            form.save()
            NewUser = form.cleaned_data.get('username')
            messages.success(
                request, 'An Account just created for- ' + NewUser + ' Please log in')
            return redirect('log')
    return render(request, 'crud/regis.html', {
        'form': form
    })


def logForm(request):

    if request.method == 'POST':
        email= request.POST.get('email')
        password = request.POST.get('password')
        person = authenticate(request, email=email, password=password)
        if person is not None:
            login(request, person)
            return redirect('add')
        else:
            messages.info(request, 'User name Or password is incorrect')
    return render(request, 'crud/login.html', {

    })


def add_show(request):
    if request.method == 'POST':
        fm = Sregistration(request.POST)
        student = subscriber.objects.all()

        if fm.is_valid():
            N = fm.cleaned_data['name']
            E = fm.cleaned_data['email']
            P = fm.cleaned_data['password']
            reg = subscriber(name=N, email=E, password=P)
            reg.save()
    else:
        fm = Sregistration()
    student = subscriber.objects.all()
    return render(request, 'crud/addNshow.html', {
        'form': fm,
        'stud': student
    })


def update(request, id):
    if request.method == 'POST':
        new = subscriber.objects.get(pk=id)
        up = Sregistration(request.POST, instance=new)
        if up.is_valid():
            up.save()
    else:
        new = subscriber.objects.get(pk=id)
        up = Sregistration(instance=new)

    return render(request, 'crud/update.html', {
        'form': up,
        'id': id
    })


def delete(request, id):
    if request.method == 'POST':
        new = subscriber.objects.get(pk=id)
        new.delete()
    return HttpResponseRedirect('/')
