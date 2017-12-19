from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from .models import *

# Register your models here.

class PageAdmin(DraggableMPTTAdmin):
    list_display = ['tree_actions', 'indented_title', 'published', 'modified']
    list_display_links = ['indented_title']
    fields = ['name','url','content', 'published']

    class Meta:
        model: Page

admin.site.register(Page, PageAdmin)

# admin.site.register(
#     Page,
#     DraggableMPTTAdmin,
#     list_display=(
#         'tree_actions',
#         'indented_title',
#         'published',
#         'modified',
#         # ...more fields if you feel like it...
#     ),
#     list_display_links=(
#         'indented_title',
#     ),
# )

admin.site.register(
    Project,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        'published',
        'modified',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)

