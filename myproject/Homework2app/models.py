from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=128)
    address = models.CharField(max_length=240)
    data_user = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'Username: {self.name}, email: {self.email}, phone: {self.phone}, address: {self.address}, '
                f'create: {self.data_user}')


class Product(models.Model):
    name = models.CharField(max_length=64)
    count = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    data_product = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return (f'Product: {self.name}, count: {self.count}, description: {self.description}, '
                f'price: {self.price}, create: {self.data_product}')


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    data_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return (f'client: {self.customer}, products: {self.products.name}, '
                f'price: {self.total_price}, create: {self.data_ordered}')
