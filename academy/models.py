from django.db import models
import os
# Create your models here.
class UnitName(models.Model):
    title =  models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class School(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="edu/schools/logo/", null=True, blank=True)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Note(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='notes')
    unit_name = models.ForeignKey(UnitName, on_delete=models.CASCADE, related_name="notes")
    school = models.ForeignKey(School, null=True, blank=True, on_delete=models.CASCADE, related_name="notes")
    file = models.FileField(upload_to="edu/documents")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file.name[14:-4]
    
    def get_extension(self):
        name, extension = os.path.splitext(self.file.name)

        return extension