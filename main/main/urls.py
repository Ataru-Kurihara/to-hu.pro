"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .views import Files, File, Projects

urlpatterns = [
    path('admin/', admin.site.urls),
    path('files/', Files.as_view(), name='files'),
    path('files/<int:dir_id>', File.as_view(), name='file'),
    path('files/<int:dir_id>/<str:folder_name>', Projects.as_view(), name='projects'),
]
