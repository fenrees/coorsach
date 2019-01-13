from django.urls import path
from . import views

urlpatterns = [
    path('', views.title, name='title'),
    path('admin', views.admin, name='admin'),
    path('get_system', views.get_system, name='get_system'),
    path('add_book', views.add_book, name='add_book'),    
]
