from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'recipes/home.html')
def contact(request):
    return HttpResponse("Contato")
def about(request): #Reecebemos a requisição do cliente
    return HttpResponse("Sobre") #Retornamos a resposta
    