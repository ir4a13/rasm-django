from django.shortcuts import render, get_object_or_404
from .models import Page
# from django.views.generic import DetailView


# Create your views here.
def node(request):
    return render(
        request,
        'page_content.html',
    )

def show_page(request, path, instance):
    if instance:
        instance.views += 1
        instance.save()
    return render(
        request,
        'page_content.html',
        {
            'instance': instance,
            'children': instance.get_children() if instance else Page.objects.root_nodes(),

        }
    )


def show_category(request, hierarchy=None):
    page_slug = hierarchy.split('/')
    parent = None
    root = Page.objects.all()

    for slug in page_slug[:-1]:
        parent = root.get(parent=parent, slug=slug)

    try:
        instance = Page.objects.get(parent=parent, slug=page_slug[-1])
    except:
        instance = get_object_or_404(Page, slug=page_slug[-1])
        return render(request, "page_content.html", {'instance':instance})
    else:
        return render(request, 'page_content.html', {'instance':instance})

 # class PageView(DetailView):
 #        template_name = 'page_content.html'
 #
 #        def dispatch(self, *args, **kwargs):  # already resolved instance here!
 #            self.instance = kwargs.pop('instance')  # save instance
 #            return super().dispatch(*args, **kwargs)
 #
 #        def get_object(self, queryset=None):
 #            return self.instance  # use saved instance
 #
