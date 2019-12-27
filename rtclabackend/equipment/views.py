from django.shortcuts import render
from .models import Equipments

# Create your views here.


def equipments(request):
    context = {
        'equipments': Equipments.objects.all(),
    }
    return render(request, 'equipments/equipments.html', context)
