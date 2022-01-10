from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import CreateUserForm
from django.contrib.auth.models import User

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
    context = {'form': form}
    return render(request, 'registration/sign_up.html',context)


def index(request):
    return render(request, 'registration/index.html')
