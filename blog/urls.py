from django.urls import path
# from . import views
from .views import BlogView, BlogDetailView


urlpatterns = [
    # path('', views.blog, name='blog'),
    # path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    # path('add/', views.add_blogpost, name='add_blogpost'),
    path('', BlogView.as_view(), name='blog'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
]