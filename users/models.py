from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from main.settings import LANGUAGES as LANGUAGE_CHOICES

# Create your models here.

GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female'),
    ('other', 'other')
)


class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='other')
    language_preference = models.CharField(max_length=100, choices=LANGUAGE_CHOICES, default='en')
    image = models.ImageField(upload_to='users/profiles/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username  

class Team(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    rank = models.CharField(max_length=100)
    image = models.ImageField(upload_to='users/teams/')
    experience = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0)
    meta_title = models.CharField(max_length=150, blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ('order',)
    
    def get_absolute_url(self):
        return reverse('users:team_details', kwargs={'slug': self.slug})
    
class Skill(models.Model):
    team_member = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="skills")
    title = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(default=0, help_text="In percentage, e.g 90")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-level',)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance,)