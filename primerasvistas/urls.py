from .views import Home
from .views import DatosPapa
from .views import DatosHermana
from .views import DatosYo
from django.urls import path

urlpatterns = [
    path('Home/', Home),
    path('DatosPapa/', DatosPapa),
    path('DatosHermana/', DatosHermana),
    path('DatosYo/', DatosYo),
]
