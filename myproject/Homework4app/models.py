from django.db import models


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
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    value = models.IntegerField()
    date_add = models.DateField()
    data = models.FileField(upload_to='Homework4app', blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.client} {self.total_amount} {self.order_date}'
