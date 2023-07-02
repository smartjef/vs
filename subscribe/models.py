from django.db import models

# Create your models here.
TEMPLATE_CHOICES = (
    ('default', 'default'),
    ('blogs', 'blogs'),
    ('products', 'products')
)

class Subscriber(models.Model):
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    is_subscribed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ('-created_at','is_subscribed')


class MailMessage(models.Model):
    subject = models.CharField(max_length=250)
    message = models.TextField(null=True, blank=True)
    template = models.CharField(max_length=10, choices=TEMPLATE_CHOICES, default='default')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ('-created_at',)
    
