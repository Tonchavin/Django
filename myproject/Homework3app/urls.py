from django.urls import path
from .views import index, list_of_products, upload_image

urlpatterns = [
    path('', index, name='index'),
    path('list_of_products/<int:id_client>/<int:period>', list_of_products, name='list_of_products'),
    path('upload_image', upload_image, name='upload_image'),

]
