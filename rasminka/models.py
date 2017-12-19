from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from django.urls import reverse

# Create your models here.


class Page(MPTTModel):
    name = models.CharField(max_length=64, blank=False, default="New Page")
    content = models.TextField(blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(auto_now_add=False, auto_now=True)
    published = models.BooleanField()
    published_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    slug = models.SlugField()
    url = models.CharField(max_length=255, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=None)

    class MPTTMeta:
        order_insertion_by = ['name']
        level_attr = 'mptt_level'

    class Meta:
        unique_together = ('slug', 'parent')
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    def __str__(self):
        return "%s" % self.name

    def save(self, *args, **kwargs):
        # now create a URL based on parent's url + slug
        if self.parent:
            self.url = '%s/%s' % (self.parent.url, self.slug)
        else:
            self.url = self.slug
        super(Page, self).save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('rasminka.views.show_page', args=[str(self.url)])



class Project(models.Model):
    name = models.CharField(max_length=64, blank=False, default="New Page")
    content = models.TextField(blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(auto_now_add=False, auto_now=True)
    published = models.BooleanField()
    published_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    slug = models.SlugField(unique=True)
    url = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "%s" % self.name

    def save(self, *args, **kwargs):
        # now create a URL based on parent's url + slug
        self.url = self.slug
        super(Project, self).save(*args, **kwargs)

    class MPTTMeta:
        order_insertion_by = ['name']
        level_attr = 'mptt_level'

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
