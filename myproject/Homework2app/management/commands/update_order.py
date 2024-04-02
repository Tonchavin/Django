from django.core.management.base import BaseCommand

from Homework2app.models import User, Product, Order


class Command(BaseCommand):
    help = "Update order."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')
        parser.add_argument('user', type=int, help='User ID')
        parser.add_argument('product', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        ...
        order.save()
        self.stdout.write(f'{order}')
