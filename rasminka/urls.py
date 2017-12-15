from django.urls import path
from . import views

urlpatterns = [
    path('/', views.rasminka, name='rasminka'),
    path('/page_url', 'views.show_page'),

]
