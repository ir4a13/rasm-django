from django.urls import path, re_path
from . import views
import mptt_urls


urlpatterns = [
    path('', views.node),
    path('<path:path_name>', views.show_page, name='page_url'),
]
