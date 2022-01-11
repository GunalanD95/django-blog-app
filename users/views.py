from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import CreateUserForm 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout

# Create your views here.



def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print("request.POST:", request.POST)
        if form.is_valid():
            print("form_valid gunalan")
            form.save()
            user = form.save(commit=False)
            user.is_active = True    # if you want to skip email validation
            user.email = User.objects.normalize_email(user.email)
            user.save()
            return redirect('logins')
    context = {'form': form}
    return render(request, 'registration/sign_up.html',context)


def index(request):
    if request.method == 'POST':
        print("request.POST:", request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            print("user:", user)
            login(request, user)
            return redirect('blogs')
        else:
            print("user is None")
            return redirect('logins')
    return render(request, 'registration/index.html')
