from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PersonCreationForm
from .models import Person, Cource,Department

# Create your views here.
def Index(request):
    departments = Department.objects.all()
    return render(request, 'auth_system/index.html', {'departments':departments})

@login_required
def DashboardPage(request):
    return render(request, 'auth_system/dashboard.html', {})

def Register(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')
        cpassword = request.POST.get('cpass')
        if(password!=cpassword):
            return HttpResponse('Error, password does not match')

        new_user = User.objects.create_user(name,password=password)
        new_user.save()
        return redirect('login-page')
  
    return render(request, 'auth_system/register.html', {})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard-page')
        else:
            return HttpResponse('Error, user does not exist')


    return render(request, 'auth_system/login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('login-page')

def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'auth_system/person.html', {'messages':'success'})
            # return redirect('person_add',{'messages':'success'})
    return render(request, 'auth_system/person.html', {'form': form})

def load_cources(request):
    department_id = request.GET.get('department_id')
    cources = Cource.objects.filter(department_id=department_id).all()
    return render(request, 'auth_system/cource_dropdown_list_options.html', {'cources': cources})

