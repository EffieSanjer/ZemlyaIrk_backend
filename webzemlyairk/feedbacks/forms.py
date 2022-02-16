from .models import Feedback
from django import forms

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email_phone', 'for_sale')

class ObjectFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email_phone', 'object_id')