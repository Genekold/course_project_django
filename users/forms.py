from django.contrib.auth.forms import UserCreationForm

from mailing.forms import StyleForm
from users.models import User


class UserRegisterForm(StyleForm, UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
