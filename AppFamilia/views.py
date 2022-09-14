from django.http import HttpResponse
from AppFamilia.models import Familiar

def padre(self):

    padre = Familiar(apellido="Alonzo",nombre="Guillermo",numeroCelular=3516760405,fechaNacimiento='1963-11-21')
    padre.save()
    textopadre = f"PADRE: ---> NOMBRE: {padre.nombre} -- APELLIDO: {padre.apellido} -- TELÉFONO CELULAR: {padre.numeroCelular} -- FECHA DE NACIMIENTO: {padre.fechaNacimiento}"

    return HttpResponse(textopadre)

def madre(self):
    madre = Familiar(apellido="Oviedo",nombre="Daniela",numeroCelular=3515555555,fechaNacimiento='1965-9-30')
    madre.save()
    textomadre = f"MADRE ---> NOMBRE: {madre.nombre} -- APELLIDO: {madre.apellido} -- TELÉFONO CELULAR: {madre.numeroCelular} -- FECHA DE NACIMIENTO: {madre.fechaNacimiento}"

    return HttpResponse(textomadre)

def hermano(self):
    hermano = Familiar(apellido="Alonzo",nombre="Ignacio",numeroCelular=3516151234,fechaNacimiento='1993-3-4')
    hermano.save()
    textohermano = f"HERMANO: ---> NOMBRE: {hermano.nombre} -- APELLIDO: {hermano.apellido} -- TELÉFONO CELULAR: {hermano.numeroCelular} -- FECHA DE NACIMIENTO: {hermano.fechaNacimiento}"

    return HttpResponse(textohermano)