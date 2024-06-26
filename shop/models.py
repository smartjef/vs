from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class ProductCategory(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('shop:list_by_category', kwargs={'category_slug': self.slug})

class Brand(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('shop:list_by_brand', kwargs={'brand_slug': self.slug})
    
class Product(models.Model):
    category = models.ForeignKey(ProductCategory, related_name='products', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='shop/products/', blank=True)
    description = models.TextField(blank=True)
    meta_title = models.CharField(max_length=150, blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0, help_text='in percentage(%)')
    in_stock = models.PositiveSmallIntegerField(default=0)
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        index_together = (('id', 'slug'),)

    def get_initial_price(self):
        initial_cost = self.current_price
        if self.discount:
            initial_cost = (100*self.current_price)/(100 - self.discount)
        return int(initial_cost)
    
    def get_absolute_url(self):
        return reverse('shop:detail', kwargs={'slug': self.slug})
    
    def get_average_rating(self):
        total_ratings = self.reviews.aggregate(total=models.Sum('rating'))['total']
        review_count = self.reviews.count()
        if total_ratings is None or review_count == 0:
            return 0
        return round(total_ratings / review_count)
    
    def __str__(self):
        return self.title
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='shop/product/images/')

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('-rating',)