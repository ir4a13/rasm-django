from django.urls import path
from . import views

urlpatterns = [
    path('/', 'views.show_page'),
    path('/page_url', 'views.show_page'),

]
