"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('prefix', include('myapp.urls')),
    # path('HW1/', include('Homework1app.urls')),
    # path('HW2/', include('Homework2app.urls')),
    # path('HW3/', include('Homework3app.urls')),
    # path('HW4/', include('Homework4app.urls')),
    # path('HW5/', include('Homework5app.urls')),
    path('HW6/', include('Homework6app.urls')),
    # path('__debug__/', include("debug_toolbar.urls")),
]
