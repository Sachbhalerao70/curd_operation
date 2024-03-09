from django import forms
from .models import appModel

class appForm(forms.ModelForm):
    class Meta:
        model=appModel
        fields='__all__'
