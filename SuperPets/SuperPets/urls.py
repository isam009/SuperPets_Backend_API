"""
URL configuration for SuperPets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include

from api import views
from rest_framework import routers

router = routers.DefaultRouter()

#* En el router vamos añadiendo los endpoints a los viewsets
router.register('productos', views.ProductoViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]

# Setencia para importar y que pueda servir archivos estaticos
if settings.DEBUG: # If DEBUG is True so do this...
    from django.conf.urls.static import static # importando static de las urls
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # static(URL, ROOT)
    # Le cedimos a la url que si alguine intenta acceder a la direccion de algun fichero, se lo sirva