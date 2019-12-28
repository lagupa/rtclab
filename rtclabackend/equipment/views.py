from django.shortcuts import render, redirect
from .models import Equipment
from .forms import EquipmentForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/')
def equipment(request):
    context = {
        'equipments': Equipment.objects.all(),
    }
    return render(request, 'equipment/equipments.html', context)


@login_required(login_url='/')
def create_new_equipment(request):
    form = EquipmentForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('equipment')
    context = {
        'form': EquipmentForm,
    }
    return render(request, 'equipment/new_equipments_form.html', context)


@login_required(login_url='/')
def edit_equipment(request, id):
    equip_db = Equipment.objects.get(id=id)
    print(equip_db)
    equip_edit_form = EquipmentForm(request.POST or None, instance=equip_db)

    if equip_edit_form.is_valid():
        equip_edit_form.save()
        return redirect('equipment')

    context = {
        'form': equip_edit_form,
        'edit_item': equip_db
    }
    return render(request, 'equipment/new_equipments_form.html', context)


@login_required(login_url='/')
def delete_equipment(request, id):
    print(request.POST)
    deleted = Equipment.objects.get(id=id)
    print(deleted)
    deleted.delete()
    return redirect('equipment')
