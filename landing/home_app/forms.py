from .models import Service, Review, Consultation
from django import forms


# Форма для добавления отзыва
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'body']


# Форма для добавления услуг
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'price']


# Форма для оставления заявки
class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['username', 'number']



