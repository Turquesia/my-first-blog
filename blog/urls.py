from django.urls import path
from . import views  # Ejemplo básico

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

