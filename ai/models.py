from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class ImageDescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    initial_number_of_images = models.PositiveSmallIntegerField(default=1)
    size =  models.CharField(max_length=100, default='1024x1024')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description[:50]

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Description'
        verbose_name_plural = 'Descriptions'

class GeneratedImage(models.Model):
    description = models.ForeignKey(ImageDescription, on_delete=models.CASCADE, related_name='generated_images')
    image_url = models.URLField(max_length=700)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_url

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Generated Image'
        verbose_name_plural = 'Generated Images'

class Trial(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='trials')
    number = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.number}'
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Trial'
        verbose_name_plural = 'Trials'
