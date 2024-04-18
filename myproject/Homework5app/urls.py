from django.urls import path
from . import views

urlpatterns = [
    path('update/', views.update_product, name='update_product'),
    path('user/', views.user_form, name='user_form'),
]
