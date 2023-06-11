from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


#MOdel for Blog
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey('core.Category', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    body = models.TextField()
    tags = models.ManyToManyField('core.Tag', blank=True)
    front_image = models.ImageField(upload_to='blogs/front/images/', null=True, blank=True)
    cover_image = models.ImageField(upload_to='blogs/cover/images/', null=True, blank=True)
    is_published = models.BooleanField(default=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    meta_title = models.CharField(max_length=150, blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    dislikes = models.PositiveIntegerField(default=0)
    published_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ('-created_at',)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'

    class Meta:
        ordering = ('-created_at',)

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Reply by {self.name} on {self.comment}'

    class Meta:
        ordering = ('-created_at',)