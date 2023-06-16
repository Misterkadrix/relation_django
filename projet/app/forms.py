from django import forms
from app.models import Pays
from app.models import President,Continent


class PaysForm(forms.ModelForm):
    class Meta:
        model = Pays
        fields= '__all__'

class PresidentForm(forms.ModelForm):
    class Meta:
        model = President
        fields= '__all__'

class ContinentForm(forms.ModelForm):
    class Meta:
        model = Continent
        fields= '__all__'
    