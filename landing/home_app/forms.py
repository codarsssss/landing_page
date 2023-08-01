from django import forms
from .models import Consultation, News


class ConsultationForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    number = forms.CharField(max_length=12)

    class Meta:
        model = Consultation
        fields = ['username', 'number']


class NewsrForm(forms.ModelForm):
    title = forms.CharField(max_length=255)
    slug = forms.URLField()
    image = forms.ImageField()
    text = forms.Textarea()
    create_datetime = forms.DateTimeField(auto_now_add=True)

    class Meta:
        model = News
        fields = ['title', 'create_datetime', 'text', 'image']
