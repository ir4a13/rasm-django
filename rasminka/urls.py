from django.urls import path, re_path
from . import views
import mptt_urls


urlpatterns = [
    path('', views.node),
    path('<path>', mptt_urls.view(model='rasminka.models.Page', view='rasminka.views.show_page', slug_field='slug'), name='rasminka_page'),
    # path('<slug>', ClearURLHandler(    mptt_urls.view(model='rasminka.models.Page', view='rasminka.views.show_page', slug_field='slug')
    #         (Page.objects.all(), PageView.as_view())
    #         ),
    #      name = 'generic'
    #      ),
]
