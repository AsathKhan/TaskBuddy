from django.contrib import admin
from .models import Profile, SupportMessage, Task

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'role')
admin.site.register(Profile, ProfileAdmin)

class SupportMessageAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created_at')
admin.site.register(SupportMessage, SupportMessageAdmin)

admin.site.register(Task)
