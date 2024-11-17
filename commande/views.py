from django.http import HttpResponse
from django.shortcuts import render

def list_commande(request):
    return render(request,'commande/list_commande.html')



