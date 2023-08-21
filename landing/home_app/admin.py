from django.contrib import admin
from .models import Consultation
from django.contrib.auth.models import User, Group


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
