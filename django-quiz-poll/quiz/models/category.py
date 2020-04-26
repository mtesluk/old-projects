from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    get_count = models.IntegerField(default=0)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('quiz:topics', kwargs={'category_id': self.id})

    def __str__(self):
        return self.name
