from django.http import HttpResponse
from django.shortcuts import render

import client


def list_client(request):
    return render(request,'client/list_client.html')

