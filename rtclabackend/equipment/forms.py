from django import forms
from .models import Equipment
from bootstrap_datepicker_plus import DateTimePickerInput


class EquipmentForm(forms.ModelForm):
    lab_id = forms.CharField(
        label='Lab Id',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    name = forms.CharField(
        label='Name',
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    model = forms.CharField(
        label='Model',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    marker = forms.CharField(
        label='Marker',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    location_in_lab = forms.CharField(
        label='Location in Lab',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    location_in_lab = forms.CharField(
        label='Location in Lab',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    using_personel = forms.CharField(
        label='In use by',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    company_that_caliberated = forms.CharField(
        label='Company that caliberated',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    company_that_serviced = forms.CharField(
        label='Company the Service',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    project = forms.CharField(
        label='Project',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Equipment
        fields = '__all__'
        widgets = {
            'data_supplied': DateTimePickerInput(),
            'date_serviced': DateTimePickerInput(),
            'next_service_date': DateTimePickerInput(),
            'date_caliberated': DateTimePickerInput(),
            'next_caliberation_date': DateTimePickerInput()
        }
