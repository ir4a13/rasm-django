from django.shortcuts import render, get_object_or_404
from .models import Page
# from django.views.generic import DetailView


# Create your views here.
def node(request):
    return render(request, 'base.html')


def show_page(request, path_name):
    page = get_object_or_404(Page, url=path_name)
    return render(request, 'rasminka/page_content.html', {'page': page})


