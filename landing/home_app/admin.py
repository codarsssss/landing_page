from django.contrib import admin
from .models import Consultation, Review, Service
from django.contrib.auth.models import User, Group


# Отзывы в админ панеле
@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    list_display = ['name', 'body', 'create_date',
                    'active']
    list_filter = ['active', 'create_date']
    search_fields = ['body', 'name']
    ordering = ['active', '-create_date']
    readonly_fields = ['create_date']


# Услуги в админ панеле


# Заявки в админ панеле
@admin.register(Consultation)
class AdminConsultation(admin.ModelAdmin):
    list_display = ['username', 'number', 'status',
                    'date_application']
    list_filter = ['status', 'date_application']
    readonly_fields = ['date_application']
    search_fields = ['username']
    ordering = ['status', '-date_application']


admin.site.unregister(User)
admin.site.unregister(Group)
