from django.urls import path
from django.urls.conf import include

from . import views
from .views import UserCreateView

urlpatterns = [
    path('signup/',UserCreateView.as_view(),name='signup'),
    # path('login/',views.lo,name='login'),
]
