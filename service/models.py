from django.db import models
from django.urls import reverse
# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=120)
    description = models.TextField()
    icon = models.CharField(max_length=30, blank=True, null=True)
    front_image = models.ImageField(upload_to='Services/front/', null=True, blank=True)
    cover_image = models.ImageField(upload_to='Services/cover/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse('services:detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('-created_at',)