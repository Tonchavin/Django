from decimal import Decimal

from django.core.management.base import BaseCommand

from Homework2app.models import User, Product, Order


class Command(BaseCommand):
    help = "Create Order."

    def add_arguments(self, parser):
        parser.add_argument('user', type=int, help='User ID')
        parser.add_argument('products', type=int, help='Product ID')
        parser.add_argument('count', type=int, help='Product count')

    def handle(self, *args, **kwargs):
        user_id = kwargs.get('user')
        products_id = kwargs.get('products')
        products_count = kwargs.get('count')

        customer = User.objects.get(id=user_id)
        product = Product.objects.get(id=products_id)
        total_price = product.price * products_count
        order = Order.objects.create(customer=customer, total_price=total_price)
        order.products.set([product])
        order.save()

        # self.stdout.write(f'{order}')
