from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reagent
from .forms import ReagentForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/')
def reagent(request):
    context = {
        'reagents': Reagent.objects.all(),
    }
    return render(request, 'reagent/reagents.html', context)


@login_required(login_url='/')
def create_new_reagent(request):
    form = ReagentForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            print(instance.user)
            messages.success(request, 'Successfully saved...')
            return redirect('reagent')
    context = {
        'form': ReagentForm,
    }
    return render(request, 'reagent/new_reagents_form.html', context)


@login_required(login_url='/')
def edit_reagent(request, id):
    equip_db = Reagent.objects.get(id=id)
    print(equip_db)
    equip_edit_form = ReagentForm(request.POST or None, instance=equip_db)

    if equip_edit_form.is_valid():
        equip_edit_form.save()
        return redirect('reagent')

    context = {
        'form': equip_edit_form,
        'edit_item': equip_db
    }
    return render(request, 'reagent/new_reagents_form.html', context)


@login_required(login_url='/')
def delete_reagent(request, id):
    print(request.POST)
    deleted = Reagent.objects.get(id=id)
    print(deleted)
    deleted.delete()
    return redirect('reagent')
