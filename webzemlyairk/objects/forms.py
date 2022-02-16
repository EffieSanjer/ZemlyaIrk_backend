from .models import Object
from django import forms

class ObjectForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = ('type', 'seller', 'parent', 'distance', 
        'area', 'description', 'rating', 'status', 'cost', 'comission', 'good_price', 
        'bargain', 'invest_attract', 'latitude', 'longitude')