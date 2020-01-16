from django import forms
from .models import Reagent
from bootstrap_datepicker_plus import DateTimePickerInput


class ReagentForm(forms.ModelForm):
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

    # NumberInput
    CAT_number = forms.CharField(
        label='CAT Number',
        max_length=20,
        widget=forms.NumberInput(
            attrs={
                "min": "0",
                "class": "form-control"
            }
        )
    )
    quantity = forms.CharField(
        label='Quantity',
        max_length=20,
        widget=forms.NumberInput(
            attrs={
                "min": "0",
                "class": "form-control"
            }
        )
    )
    marker = forms.CharField(
        label='Marker',
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    storage_requirement = forms.CharField(
        label='Storage Requirements',
        widget=forms.Textarea(
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

    ordered_by = forms.CharField(
        label='In use by',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    project_code = forms.CharField(
        label='Company that caliberated',
        max_length=130,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Reagent
        fields = '__all__'
        widgets = {
            'date_supplied': DateTimePickerInput(),
            'manufacturer_date': DateTimePickerInput(),
            'expiry_date': DateTimePickerInput(),
            'date_caliberated': DateTimePickerInput(),
            'next_caliberation_date': DateTimePickerInput(),
            'project': forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            )
        }
