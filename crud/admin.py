#import email
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import subscriber,profiles

# Register your models here.

class profilesAdmin(admin.ModelAdmin):
    list_display = ('email','username', 'last_login','date_joined','is_admin','is_staff')
    search_fields=('email','username')
    readonly_fields=('id','date_joined','last_login')

    filter_horizontal=()
    list_filter=()
    fieldsets=()
admin.site.register(profiles, profilesAdmin)



@admin.register(subscriber)
class useradmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'password', 'email')
