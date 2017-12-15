from django.shortcuts import render


# Create your views here.
def show_page(request, page_url=None):
    page = get_object_or_404(Page, url=page_url)
    render(request, 'page.html')