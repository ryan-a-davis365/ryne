from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254, unique=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    group = models.CharField(max_length=50, choices=[('clothing', 'Clothing'), ('special', 'Special Offers')], default='clothing')

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name
    
class Product(models.Model):
    category = models.ManyToManyField('Category', blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    def update_rating(self):
        avg = self.reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']
        self.rating = avg if avg is not None else 0
        self.save(update_fields=['rating'])
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.product.update_rating()

    def delete(self, *args, **kwargs):
        product = self.product
        super().delete(*args, **kwargs)
        product.update_rating()

    def __str__(self):
        return f"Review by {self.user} on {self.product}"