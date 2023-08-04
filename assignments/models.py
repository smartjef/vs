from django.db import models
from ai.models import AreaChoice, LevelChoice
from django.urls import reverse
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

UNIT_CHOICES = [
    ('Hours','Hours'),
    ('Days', 'Days'),
    ('Weeks', 'Weeks'),
    ('Months', 'Months')
]
class Period(models.Model):
    quantity = models.PositiveSmallIntegerField(default=1)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='Hours')
    is_active = models.BooleanField(default=True)
    rate = models.FloatField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_seconds_equivalence(self):
        pass
    
    def __str__(self):
        return f'{self.quantity} - {self.unit}'
    
    class Meta:
        ordering = ['created_at'] 

STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Assigned', 'Assigned'),
    ('Completed', 'Completed'),
    ('Cancelled', 'Cancelled')
]
class AssignmentOrder(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='assignments')   
    title = models.CharField(max_length=200, help_text="(Unit's Name) Assignment")
    subject_area = models.ForeignKey(AreaChoice, on_delete=models.CASCADE, blank=True, null=True)
    academic_level = models.ForeignKey(LevelChoice, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    additional_information = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    refered_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_amount(self):
        amount = 300 * float(self.academic_level.charge_rate) * float(self.period.rate)
        return amount
    
    class Meta:
        ordering = ['-created_at',]

    def get_absolute_url(self):
        return reverse('gwd:assignment_detail', kwargs={'assignment_id': self.id})

class AssignmentFiles(models.Model):
    assignment = models.ForeignKey(AssignmentOrder, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='assignments/')

    def __str__(self):
        return self.file.name

class ProjectPeriod(models.Model):
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    rate = models.FloatField(default=1)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.period.quantity} - {self.period.unit}'
    

class ProjectOrder(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='projects')   
    title = models.CharField(max_length=200, help_text="(Unit's Name) Assignment")
    subject_area = models.ForeignKey(AreaChoice, on_delete=models.CASCADE, blank=True, null=True)
    academic_level = models.ForeignKey(LevelChoice, on_delete=models.CASCADE)
    period = models.ForeignKey(ProjectPeriod, on_delete=models.CASCADE)
    additional_information = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    refered_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
    
    def get_amount(self):
        amount = 10000 * float(self.academic_level.charge_rate) * float(self.period.rate)
        return amount

    def get_absolute_url(self):
        return reverse('gwd:project_detail', kwargs={'project_id': self.id})

class ProjectFiles(models.Model):
    project = models.ForeignKey(ProjectOrder, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='projects/')

    def __str__(self):
        return self.file.name

class Payment(models.Model):
    assignment = models.OneToOneField(AssignmentOrder, on_delete=models.CASCADE, related_name='payment', null=True, blank=True)
    project = models.OneToOneField(ProjectOrder, on_delete=models.CASCADE, related_name='payment', null=True, blank=True)
    transaction_code = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    amount = models.DecimalField(decimal_places=2, default=0.00, max_digits=7)
    mpesa_code = models.CharField(null=True, blank=True, unique=True, max_length=20)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_code

    class Meta:
        ordering = ['-created_at']
    
    def get_amount_earned_by_referer(self):
        return .05 * float(self.amount)
    
    def get_absolute_url(self):
        return reverse('gwd:make_payment', kwargs={'code': self.transaction_code})
    
class Response(models.Model):
    assignment = models.OneToOneField(AssignmentOrder, on_delete=models.CASCADE, related_name='response', null=True, blank=True)
    project = models.OneToOneField(ProjectOrder, on_delete=models.CASCADE, related_name='response', null=True, blank=True)
    link = models.URLField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link

    class Meta:
        ordering = ['-created_at']
