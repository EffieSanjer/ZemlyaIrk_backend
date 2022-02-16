from .models import Person
from django import forms

class ClientForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('full_name', 'phone1', 'phone2', 'email', 'comment' )

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('full_name', 'phone1', 'phone2', 'email', 'comment', 'position' )