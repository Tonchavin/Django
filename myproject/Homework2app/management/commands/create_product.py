from decimal import Decimal

from django.core.management.base import BaseCommand

from Homework2app.models import Product


class Command(BaseCommand):
    help = "Create product."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Product name')
        parser.add_argument('count', type=int, help='Product count')
        parser.add_argument('description', type=str, help='Product description')
        parser.add_argument('price', type=Decimal, help='Product price')

    def handle(self, *args, **kwargs):
        product = Product(name=kwargs.get('name'), count=kwargs.get('count'),
                          description=kwargs.get('description'), price=kwargs.get('price'))
        product.save()
        self.stdout.write(f'{product}')
