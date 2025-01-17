from django.contrib import admin
from app_users.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = 'id', 'user'
    list_display_links = 'id', 'user'


admin.site.register(Profile, ProfileAdmin)

# Register your models here.
