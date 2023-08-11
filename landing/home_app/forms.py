from .models import Service, Review, Consultation, News
from django import forms
from tinymce.widgets import TinyMCE


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


# Форма для добавления новости
class NewsForm(forms.ModelForm):
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))
    class Meta:
        model = News
        fields = '__all__'



