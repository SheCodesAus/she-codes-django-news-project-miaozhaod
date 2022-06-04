from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# import custom forms and model
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# extends the inbuilt UserAdmin with custom configuration
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username"]


admin.site.register(CustomUser, CustomUserAdmin)
