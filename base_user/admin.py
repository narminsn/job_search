from django.contrib import admin
# from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from .forms import MyUserChangeForm, UserCreationForm
from . import models
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.

User  =  get_user_model()

@admin.register(User)
class CreateUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
            'first_name', 'last_name', 'email', 'profile_image' , 'country','city', 'company_name',  'check', 'slug', 'headline'
            )}),
        (_('Permissions'), {'fields': ('is_active', 'is_superuser', 'is_staff',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ("first_name", "last_name", 'username', 'password1', 'password2'),
        }),
    )
    # The forms to add and change user instances
    form = MyUserChangeForm
    add_form = UserCreationForm
    readonly_fields = ["slug", 'check']
    list_display = ("username", 'email')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('first_name', 'last_name', 'username', 'email')
    ordering = ('-date_joined',)
    filter_horizontal = ('groups', 'user_permissions',)

# admin.site.register(models.VerificationModel)