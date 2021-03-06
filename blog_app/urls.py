from django.urls import path
from django.urls.conf import include
from .views import AddBlogView , UpdateBlogView , DeleteBlogView , blog

from . import views
urlpatterns = [
    path('',views.index,name='blogs'),
    path('<int:blog_id>',views.blog,name='blog'),
    path('create_blog/',AddBlogView.as_view(),name='create_blog'),
    path('edit/<int:pk>',UpdateBlogView.as_view(),name='update_blog'),
    path('<int:pk>/delete',DeleteBlogView.as_view(),name='delete_blog'),

]
