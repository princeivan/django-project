from django import forms

from .models import PoliceStation


class PoliceStationModelForm(forms.ModelForm):
    class Meta:
        model = PoliceStation
        fields = '__all__'