from django.core.management.base import BaseCommand

from Homework2app.models import User


class Command(BaseCommand):
    help = "Get user on street."

    def add_arguments(self, parser):
        parser.add_argument('address', type=str, help='User live on Street')

    def handle(self, *args, **kwargs):
        address = kwargs['address']
        user = User.objects.filter(address=address).first()
        self.stdout.write(f'{user}')
