from django.urls import path
from django.urls.conf import include


from . import views
urlpatterns = [
    path('',views.index,name='blogs'),
    path('<int:blog_id>',views.blog,name='blog'),

]
