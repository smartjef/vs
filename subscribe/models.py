from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    is_subscribed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.email