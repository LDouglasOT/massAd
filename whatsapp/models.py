from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isConnected = models.BooleanField(default=False)
    delivery = models.BooleanField(default=False)

    photo = models.ImageField(upload_to='shops/')
    photo2 = models.ImageField(upload_to='shops/')
    photo3 = models.ImageField(upload_to='shops/')
    photo4 = models.ImageField(upload_to='shops/')
    banner = models.ImageField(upload_to='shops/')


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()

    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delivered = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    pending = models.BooleanField(default=False)
    def __str__(self):
        return self.customer.name + ' - ' + self.product.name
