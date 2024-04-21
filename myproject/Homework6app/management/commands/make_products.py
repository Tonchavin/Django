from random import choice, randint, uniform

from django.core.management.base import BaseCommand
from myproject.Homework6app.models import Category, Product


# Создание фейковых продуктов
class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser):
        parser.add_arguments('count', type=int, help='Количество продуктов для генерации')

    def handle(self, *args, **kwargs):
        categories = Category.objects.all()
        products = []
        count = kwargs.get('count')
        for i in range(1, count + 1):
            products.append(Product(
                name=f'продукт номер {i}',
                category=choice(categories),
                description='длинное описание продукта, которое и так некто не читает',
                price=uniform(0.01, 99_999.99),
                value=randint(1, 10_000),
                rating=uniform(0.01, 9.99),
            ))
        Product.objects.bulk_create(products)
