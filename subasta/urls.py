
from django.contrib import admin
from django.urls import path, include
from subastaApp import views
from django.conf import settings
from django.conf.urls.static import static


"""
from rest_framework.routers import DefaultRouter
from subastaApp.views import VehiculoViewSet

router = DefaultRouter()
router.register(r'subastaApp'.VehiculoViewSet)
#from django.config import settings
#from django.config.urls.static import static 

urlpatterns += router.urls
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehiculos/', include("vehiculos.urls")),
    path('', views.home, name="Home"),
    path('detalle', views.detalle, name="Detalle"),
    path('login', views.login, name="Login"),
    path('contacto', views.contacto, name="Contacto"),
    path('servicios', views.servicios, name="Servicios"),

    
]  #+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)