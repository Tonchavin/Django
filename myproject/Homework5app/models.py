from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12, default='0000000000')
    address = models.CharField(max_length=150)
    date_of_registry = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.email}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(default='', blank=True)
    price = models.DecimalField(default=999999.99, max_digits=8, decimal_places=2)
    value = models.PositiveSmallIntegerField(default=0)
    date_add = models.DateField(auto_now_add=True)
    data = models.FileField(upload_to='Homework5app', blank=True, null=True)
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.client} {self.total_amount} {self.order_date}'
