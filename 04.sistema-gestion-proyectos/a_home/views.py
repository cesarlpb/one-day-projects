from django.shortcuts import render
from django.contrib.auth.models import User

def home_view(request):
    
    context = {
        
    }
    return render(request, 'index.html', context=context)


def detalle_proyecto(request, id):
    
    context = {
        "id": id
    }
    return render(request, 'detalle_proyectos.html', context=context)