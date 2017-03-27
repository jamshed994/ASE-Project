from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _

from performer.models import User, Venue, Performer
from performer.forms import CustomUserCreationForm, VenueCreationForm, PerformerCreationForm

class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserCreationForm
 
admin.site.register(User, CustomUserAdmin)
 
class VenueAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'venueid',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'venueid', 'password1', 'password2')}
        ),
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('venueid', 'first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    form = VenueCreationForm
 
admin.site.register(Venue, VenueAdmin)
 
class PerformerAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'performer_id',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'performer_id', 'password1', 'password2')}
        ),
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('performer_id', 'first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    form = PerformerCreationForm
 
admin.site.register(Performer, PerformerAdmin)
'''
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'full_name', 'date_joined', 'last_login', 'is_active')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    date_hierarchy = 'date_joined'
    ordering = ('-date_joined',)
    fieldsets = (
        (None, {
            'fields': ('username', 'password')}),

        (_('Personal info'), {
            'fields': (('first_name', 'last_name'), 'email', 'photo')}),

        (_('Important dates'), {
            'fields': (('last_login', 'date_joined'),)}),

        (_('Permissions'), {
            'classes': ('collapse',),
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )


admin.site.register(User, UserAdmin)
'''
