from django.urls import path
from . import views

urlpatterns = [
    path('inquiry/<product_id>/', views.inquiry, name='inquiry'),
]