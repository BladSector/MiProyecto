
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render


def contenido(request, nombre, edad):
    contenido = '''
    <html>
    <body>
    <p>Nombre: %s </p> Edad: %s</p>
    </body>
    </html>
    '''%(nombre, edad)
    return HttpResponse(contenido)

'''
def MiPrimeraPlantilla(request):
    #Abrimos documento
    PlantillaExterna = open("C:\MiProyecto\MiProyecto\plantillas\MiPrimeraPlantilla.html")
    #cargar el doc en variable 'Template'
    template = Template(PlantillaExterna.read())
    PlantillaExterna.close()
    #Crear un contexto
    contexto = Context()
    #Renderizar el documento
    documento = template.render(contexto)
    return HttpResponse(documento)
'''


def Home(request):
    Titulo = 'Proyecto "Nuestro Primer MVT"'
    Participantes= 'Santiago Lopez y Santiago Cuellar Dominguez'
    Fecha = (datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M"))
    PlantillaExterna = open("C:\MiProyecto\plantillas\Home.html")
    template = Template(PlantillaExterna.read())
    PlantillaExterna.close()
    contexto = Context({'Titulo' : Titulo ,
    'Participantes' : Participantes,
    'Fecha': Fecha })
    documento = template.render(contexto)
    return HttpResponse(documento)


def DatosPapa(request):
    Titulo = 'Proyecto "Nuestro Primer MVT"'
    Fecha = (datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M"))
    Participantes= 'Santiago Lopez y Santiago Cuellar Dominguez'
    quien = 'Papa'
    nombre = 'Guillermo'
    nacimiento = '03/08/59'
    edad = '63'
    trabajo = 'Medico Psiquiatra'
    caracteristicas = ['Pelo corto', 'Panzon', 'Ojos verdes']
    PlantillaExterna = open("C:\MiProyecto\plantillas\DatosPapa.html")
    template = Template(PlantillaExterna.read())
    PlantillaExterna.close()
    contexto = Context({'Nombre': nombre, 'Edad': edad,
    'Trabajo': trabajo,'Caracteristicas':caracteristicas,
    'Nacimiento': nacimiento, 'Quien': quien, 'Titulo' : Titulo ,
    'Participantes' : Participantes, 'Fecha': Fecha})
    documento = template.render(contexto)
    return HttpResponse(documento)

def DatosHermana(request):
    Titulo = 'Proyecto "Nuestro Primer MVT"'
    Fecha = (datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M"))
    Participantes= 'Santiago Lopez y Santiago Cuellar Dominguez'
    quien = 'Hermana'
    nombre = 'Carmela'
    nacimiento = '30/04/2002'
    edad = '20'
    trabajo = 'Acompañante Terapeutico'
    caracteristicas = ['Pelo largo', 'Flaca', 'Ojos verdes']
    return render(request, 'DatosPapa.html', {'Nombre': nombre, 'Edad': edad,
    'Trabajo': trabajo,'Caracteristicas':caracteristicas,
    'Nacimiento': nacimiento, 'Quien': quien, 'Titulo' : Titulo ,
    'Participantes' : Participantes, 'Fecha': Fecha})

def DatosYo(request):
    Titulo = 'Proyecto "Nuestro Primer MVT"'
    Fecha = (datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M"))
    Participantes= 'Santiago Lopez y Santiago Cuellar Dominguez'
    quien = 'Yo'
    nombre = 'Santiago'
    Apellido = 'Lopez'
    nacimiento = '21/06/1998'
    edad = '24'
    trabajo = 'Fundacion Pertenecer Administrador cadete'
    caracteristicas = ['Pelo medio', 'Flaco', 'Ojos marrones']
    return render(request, 'DatosPapa.html', {'Nombre': nombre, 'Edad': edad,
    'Trabajo': trabajo,'Caracteristicas':caracteristicas,
    'Nacimiento': nacimiento, 'Quien': quien, 'Titulo' : Titulo ,
    'Participantes' : Participantes, 'Fecha': Fecha})
