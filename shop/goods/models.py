from django.contrib.auth import get_user_model
from django.db import models
from uuid import uuid4

User = get_user_model()


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='%Y/%m/%d')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="products")

    def __str__(self):
        return self.name


class ProductParameters(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    count = models.IntegerField()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.author} : {self.product.name}"

    class Meta:
        ordering = ("created",)
