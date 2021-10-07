"""User admin classes"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#models
from django.contrib.auth.models import User
from user.models import Player

# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    """Player admin"""

    list_display = ('pk', 'user', 'picture',)
    list_display_links = ('pk','user')
    list_editable = ('picture',)

    fieldsets = (
        ('Player',{
            'fields':(
                ('user','picture','biography'),
                ),
            }),

        )

class PlayerInline(admin.StackedInline):
    """Player in-line admin for users"""
    
    model = Player
    can_delete = False
    verbose_name_plural = 'players'

class UserAdmin(BaseUserAdmin):
    """Add Player admin to base user admin"""
    inlines = (PlayerInline,)
    list_display =(

        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',

    )

admin.site.unregister(User)
admin.site.register(User,UserAdmin)

