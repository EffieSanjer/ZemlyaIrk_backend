from .models import Locality
from django import forms

class LocalityForm(forms.ModelForm):
    class Meta:
        model = Locality
        fields = ('name', 'show_name', 'type', 'distance', 'description', 'latitude', 'longitude')