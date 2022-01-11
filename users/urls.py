from django.urls import path
from django.urls.conf import include

from . import views
# from .views import UserCreateView

urlpatterns = [
    # path('signup/',UserCreateView.as_view(),name='signup'),
    path('signup/',views.register,name='signup'),
    path('',views.index,name='logins'),
]
