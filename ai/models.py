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
    image_trial = models.IntegerField(default=5)
    ideas_trial = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s trials - {self.image_trial} - {self.ideas_trial}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Trial'
        verbose_name_plural = 'Trials'

class AreaChoice(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    craeted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-craeted_at']
        verbose_name = 'Area Choice'
        verbose_name_plural = 'Area Choices'

class LevelChoice(models.Model):
    title = models.CharField(max_length=50, help_text="e.g, High School, Degree, Masters, PHD")
    description = models.TextField(null=True, blank=True)
    charge_rate = models.DecimalField(decimal_places=2, max_digits=3, default=1, help_text="e.g 1,1.2")
    craeted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-craeted_at']
        verbose_name = 'Level Choice'
        verbose_name_plural = 'Level Choices'

class IdeaRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='idea_requests')
    area = models.ForeignKey(AreaChoice, on_delete=models.CASCADE, related_name='idea_requests')
    level = models.ForeignKey(LevelChoice, on_delete=models.CASCADE, related_name='idea_requests')
    number_of_ideas = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.area} - {self.level} by {self.user}"
    
    def get_amount(self):
        amount = 100 * self.level.charge_rate * self.number_of_ideas
        return amount

class GeneratedIdeas(models.Model):
    idea_request = models.ForeignKey(IdeaRequest, on_delete=models.CASCADE, related_name='generated_ideas')
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Payment(models.Model):
    idea_request = models.OneToOneField(IdeaRequest, on_delete=models.CASCADE, related_name='payment')
    transaction_code = models.CharField(max_length=20, unique=True)
    amount = models.DecimalField(decimal_places=2, default=0.00, max_digits=7)
    mpesa_code = models.CharField(null=True, blank=True, unique=True, max_length=20)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_code

    class Meta:
        ordering = ['-created_at']
