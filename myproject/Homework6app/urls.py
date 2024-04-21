from django.urls import path

from . import views
from .views import total_in_db, total_in_view, total_in_template

urlpatterns = [
    path('update/', views.update_product, name='update_product'),
    path('user/', views.user_form, name='user_form'),
    path('db/', total_in_db, name='db'),
    path('view/', total_in_view, name='view'),
    path('template/', total_in_template, name='template'),
]
