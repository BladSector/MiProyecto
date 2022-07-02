from django.contrib import admin
from django.urls import path
from MiProyecto.views import Home
from MiProyecto.views import contenido
from MiProyecto.views import DatosPapa
from MiProyecto.views import DatosHermana
from MiProyecto.views import DatosYo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', Home),
    path('contenido/<nombre>/<int:edad>', contenido),
    path('DatosPapa/', DatosPapa),
    path('DatosHermana/', DatosHermana),
    path('DatosYo/', DatosYo)
]
