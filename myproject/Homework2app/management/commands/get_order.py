from django.core.management.base import BaseCommand
from Homework2app.models import User, Product, Order


class Command(BaseCommand):
    help = "Get orders "

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        order = Order.objects.filter(pk=pk).first()
        self.stdout.write(f'{order}')
