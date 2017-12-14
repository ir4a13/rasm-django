from django.urls import path
from . import views

urlpatterns = [
    path('rasminka/', views.rasminka, name='rasminka')
]
