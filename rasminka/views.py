from django.shortcuts import render, get_object_or_404
from .models import Page
# from django.views.generic import DetailView


# Create your views here.
def node(request):
    return render(request, 'base.html')


def show_page(request, path=None):
    page = get_object_or_404(Page, url=path)
    return render(request, 'rasminka/page_content.html', {'page': page})


