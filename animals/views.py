from django.shortcuts import render
from .models import Animals

def animals(request):
    animalss = Animals.objects.all()
    return render(request, 'animals.html', {'animalss':animalss})

