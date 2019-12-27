from django.shortcuts import render
from .models import Equipment
from .forms import EquipmentForm

# Create your views here.


def equipments(request):
    context = {
        'form': EquipmentForm,
        'equipments': Equipment.objects.all(),
    }
    return render(request, 'equipment/equipments.html', context)
