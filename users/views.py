from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView


# Create your views here.


# class UserCreateView(FormView):
#     template_name = 'registration/sign_up.html'
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')

#     def form_valid(self, form):
#         form.save()
#         print("form_valid")
#         return super(UserCreateView, self).form_valid(form)

def register(request):
    return render(request, 'registration/sign_up.html')


def index(request):
    return render(request, 'registration/index.html')
