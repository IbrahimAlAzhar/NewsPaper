from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    # there are so many attribute in model file because of inherit from abstract class,but here display in admin just 3
    list_display = ['email','username','age'] # here the list display on admin page,even though there are many more on the customuser mmdel at this point
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)  # add CustomUserAdmin on admin site in place of CustomUser

