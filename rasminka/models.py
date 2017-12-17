from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.template.defaultfilters import slugify

# Create your models here.

class Node(MPTTModel):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, null=True)
    url = models.CharField(max_length=255, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=None)

    class MPTTMeta:
        order_insertion_by = ['name']
    # def save(self, *args, **kwargs):
    #     if self.slug is None:
    #         # create a slug that's unique to siblings
    #         slug = slugify(self.name)
    #         self.slug = slug
    #         siblings = self.get_siblings()
    #         i = 1
    #         while siblings.filter(slug=self.slug).exists():
    #             i += 1
    #             self.slug = slug + '-%d' % i
    #
    #         # now create a URL based on parent's url + slug
    #         if self.parent:
    #             self.url = '%s/%s' % (self.parent.url, self.slug)
    #         else:
    #             self.url = self.slug
    #     super(Page_hierach, self).save(*args, **kwargs)

class Page(models.Model):
    name = models.CharField(max_length=64, blank=False, default="New Page")
    content = models.TextField(blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(auto_now_add=False, auto_now=True)
    published = models.BooleanField()
    publihed_on = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Postpage'
        verbose_name_plural = 'Postpages'

class Projects(models.Model):
    name = models.CharField(max_length=64, blank=False, default="New Page")
    content = models.TextField(blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(auto_now_add=False, auto_now=True)
    published = models.BooleanField()
    publihed_on = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'