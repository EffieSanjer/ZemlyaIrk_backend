from .models import Request
from django import forms

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('name', 'seller', 'customer', 'office', 'date_end', 'urgency', 'status','for_sale', 'description'  )