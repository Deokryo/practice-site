from django.contrib import admin
from . import models 

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'nickname',
        'name',
        'email',
    )

    list_display_links = (
        'name',
        'nickname',
        'email',
    )

# Register your models here.
