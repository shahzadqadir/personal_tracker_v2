from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (UserCreationForm, 
                                       UserChangeForm,)


class CustomUserCreationForm(UserCreationForm):
    model = get_user_model()
    fields = ["username", "email"]


class CustomUserChangeForm(UserChangeForm):
    model = get_user_model()
    fields = ["username", "email"]
