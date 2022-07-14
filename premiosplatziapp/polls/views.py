from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Estás en la pagina principal de Premios Platzi App")


def detail(request, question_id):
    return HttpResponse(f"Estás viendo la pregunta número {question_id}")


def results(request, question_id):
    return HttpResponse(f"Estás viendo los resultados de la pregunta número {question_id}")    


def vote(request, question_id):
    return HttpResponse(f"Estás votando a la pregunta numero {question_id}")  