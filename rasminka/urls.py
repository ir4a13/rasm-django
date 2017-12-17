from django.urls import path
from . import views
import mptt_urls

urlpatterns = [
    path('', views.show_page),
    path('<path>', mptt_urls.view(model='rasminka.models.Page', view='rasminka.views.show_page', slug_field='slug')),

]
