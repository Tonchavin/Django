from django.core.management.base import BaseCommand
from Homework2app.models import User, Product, Order


class Command(BaseCommand):
    help = "Get all orders "

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        self.stdout.write(f'{orders}')
