from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)
    get_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('survey:topics', kwargs={'category_id': self.id})

    def get_queryset(self):
        return self.objects.all()
