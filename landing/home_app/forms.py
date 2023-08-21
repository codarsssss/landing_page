from .models import Consultation
from django import forms


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['username', 'number']



