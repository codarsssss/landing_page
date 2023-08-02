from django.contrib import admin
from .models import News, Consultation, Review, Service
from django.contrib.auth.models import User, Group


# Новости в админ панеле
@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'text', 
                    'create_datetime', 'active']
    
    # Этот атрибут нужен для того, чтобы поле slug создавалось
    # автоматически. Работает только в админке!!!
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['active', 'create_datetime']
    search_fields = ['title', 'slug', 'text']
    ordering = ['active', 'create_datetime']
    readonly_fields = ['create_datetime']


# Отзывы в админ панеле
@admin.register(Review)
class AdminReview(admin.ModelAdmin):
    list_display = ['name', 'email', 'body', 'create_date',
                    'active']
    list_filter = ['active', 'create_date']
    search_fields = ['body', 'name']
    ordering = ['active', 'create_date']
    readonly_fields = ['create_date']


# Услуги в админ панеле
@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = ['title', 'price', 'active', 'create_date']
    list_filter = ['active', 'price', 'create_date']
    readonly_fields = ['create_date']
    search_fields = ['title', 'description']
    ordering = ['active', 'create_date']


# Заявки в админ панеле
@admin.register(Consultation)
class AdminConsultation(admin.ModelAdmin):
    list_display = ['username', 'number', 'status',
                    'date_application']
    list_filter = ['status', 'date_application']
    readonly_fields = ['date_application']
    search_fields = ['username']
    ordering = ['status', 'date_application']


admin.site.unregister(User)
admin.site.unregister(Group)