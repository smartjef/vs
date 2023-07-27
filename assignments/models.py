from django.db import models

# Create your models here.
class Referal(models.Model):
    user = models.OneToOneField('auth.user', on_delete=models.CASCADE, related_name='referal')
    code = models.CharField(max_length=10, unique=True)
    earnings = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    withdrawals= models.DecimalField(default=0, decimal_places=2, max_digits=8)
    balance = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.code}'
    
    class Meta:
        ordering = ['-created_at']

    