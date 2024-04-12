import logging
from datetime import datetime, timedelta

from django.shortcuts import render, get_object_or_404
from .forms import UserForm, ImageForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from .models import Client, Order

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse('Online shop')


def list_of_products(request, id_client, period):
    lst = []
    client = get_object_or_404(Client, pk=id_client)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=period)
    start_date_only = start_date.date()

    if client is not None:
        orders = Order.objects.filter(client=client)
        for order in orders:
            if order.order_date > start_date_only:
                products = order.products.all()
                for prod in products:
                    lst.append(prod)
    context = {'client': client.name,
               'period': period,
               'list_of_products': lst}
    return render(request, 'Homework4app/list_of_products.html', context)


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'Homework4app/upload_image.html', {'form': form})


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
    return render(request, 'Homework4app/user_form.html', {'form': form})
