from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import Group,Permission


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'SubCategories'

    def __str__(self):
        return self.name

# Create your models here.
class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default='Pending')
    no_of_items = models.IntegerField()
    total = models.DecimalField(max_digits=8, decimal_places=2)

    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    # Shipping Information
    shipping_address = models.CharField(max_length=255)
    shipping_city = models.CharField(max_length=100)
    # shipping_state = models.CharField(max_length=100)
    shipping_country = models.CharField(max_length=100)
    # shipping_zip_code = models.CharField(max_length=20)

    # Payment Information
    PAYMENT_STATUS_CHOICES = [
        ('COD', 'Cash on Delivery'),
        ('PAID', 'Paid'),
        ('NOT_PAID', 'Not Paid')
    ]
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='COD')

    def __str__(self):
        return f"Order #{self.id} ({self.user})"


    def get_total(self):
        total = 0
        no_of_items = 0

        items = OrderItem.objects.filter(order=self)
        for item in items:
            total += item.get_total()
            no_of_items+=item.get_total_qty()
        return total,no_of_items

    def save(self,*args,**kwargs):
        self.total = self.get_total()[0]
        self.no_of_items = self.get_total()[1]
        super().save(*args,**kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} ({self.order.user})"

    def get_total(self):
        return self.product.price * self.quantity

    def get_total_qty(self):
        return self.quantity

# class Review(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
#     comment = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.product.name} - {self.user.username}"
