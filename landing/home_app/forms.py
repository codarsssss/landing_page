from .models import Service, Review, Consultation, News
from django import forms


# Форма для добавления отзыва
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'body']


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


# Форма для добавления новости
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'create_datetime', 'text', 'image']