import logging

from django.shortcuts import render
from .forms import UserForm, ProductForm
from .models import Product
from django.http import HttpResponse

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse('Online shop')


# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = form.cleaned_data['image']
#             fs = FileSystemStorage()
#             fs.save(image.name, image)
#     else:
#         form = ImageForm()
#     return render(request, 'Homework4app/upload_image.html', {'form': form})


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


# Create your views here.

def update_product(request):
    message = 'New info about product'
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            id_ = form.cleaned_data['id_']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            value = form.cleaned_data['value']
            date_add = form.cleaned_data['date_add']
            image = form.cleaned_data['image']
            product = Product.objects.filter(id=id_).first()
            if product is not None:
                if image is not None:
                    product.data = image
                product.name = name
                product.description = description
                product.price = price
                product.value = value
                product.date_add = date_add
                product.save()
                message = 'Successfully'
            else:
                message = f'Product Id={id_} not found'
    else:
        form = ProductForm()
    return render(request, 'Homework4app/update_product.html', {'form': form, 'message': message})
