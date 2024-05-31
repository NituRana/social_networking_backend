from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, FriendRequest

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'email', 'full_name', 'phone_number', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at']
    list_filter = ['is_active', 'is_staff', 'is_superuser']
    search_fields = ['email', 'full_name', 'phone_number']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['email']

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    filter_horizontal = ()
    search_fields = ('email',)
    ordering = ('email',)


class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'from_user', 'to_user', 'accepted', 'rejected', 'created_at', 'updated_at']
    list_filter = ['accepted', 'rejected']
    search_fields = ['from_user__email', 'to_user__email']

admin.site.register(FriendRequest, FriendRequestAdmin)