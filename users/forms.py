from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from django import forms


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'password1',)


class UserUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'country', 'avatar',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class VerificationForm(forms.Form):
    verify_code = forms.CharField(max_length=12, label='Введите код верификации')
