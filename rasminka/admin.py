from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *

# Register your models here.

admin.site.register(Projects)
admin.site.register(Node, MPTTModelAdmin)