from django.urls import path
from . import views
from .views import BlogView, BlogDetailView


urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('add/', views.add_blogpost, name='add_blogpost'),
    path('edit/<int:post_id>/', views.edit_blogpost, name='edit_blogpost'),
]