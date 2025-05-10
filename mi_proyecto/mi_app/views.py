from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def mi_vista(request):
    return render(request, 'mi_archivo.html')
