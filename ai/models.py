from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GeneratedImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    image_url = models.URLField(max_length=700)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}'
    
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
