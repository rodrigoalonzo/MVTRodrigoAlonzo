from django.http import HttpResponse
from django.template import loader


def templateTest(self):

    nombre = "Rodrigo"
    apellido = "Alonzo"

    diccionario = {"nombre":nombre,"apellido":apellido}

    plantilla = loader.get_template("template1.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)