from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=80)
    price = models.FloatField()
    discount_price = models.FloatField()
    product_category = models.CharField(max_length=100)
    product_description = models.TextField()
    product_image = models.CharField(max_length=350)
    product_ratings = models.FloatField()
    product_review = models.CharField(max_length= 300)
    
