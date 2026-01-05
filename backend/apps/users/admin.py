from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'user_type', 'created_at']
    list_filter = ['user_type']
    search_fields = ['username', 'name']
