from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    username = forms.CharField(label='Usuario', max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {key: '' for key in fields}


class MyUserEditForm(forms.Form):

    email = forms.EmailField(required=False)
    first_name = forms.CharField(label='Nombre', max_length=30, required=False)
    last_name = forms.CharField(
        label='Apellido', max_length=30, required=False)
    avatar = forms.ImageField(required=False)
