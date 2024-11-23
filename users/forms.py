from django.contrib.auth.forms import UserCreationForm, forms

from .models import CustomUser, Profile

class CustomUserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input-box',
            'placeholder': 'Create password'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input-box',
            'placeholder': 'Confirm password'
        })
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={

            'placeholder': 'YYYY-MM-DD',

        })
    )
    class Meta:
        model = CustomUser
        fields = ['name', 'username','email', 'password1', 'password2','date_of_birth']
        widgets = {
            "name": forms.TextInput(attrs={
                'class':'input-box',
                'placeholder':'Enter your name'
            }),
            "username": forms.TextInput(attrs={
                'class': 'input-box',
                'placeholder': 'Enter your username'
            }),
            "email": forms.TextInput(attrs={
                'class': 'input-box',
                'placeholder': 'Enter your email'
            })

        }

class CustomUserLoginForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input-box',
            'placeholder': 'Enter password'
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input-box',
            'placeholder': 'Enter your username or email'
        })
    )

    class Meta:
        model = CustomUser
        fields = ['username','password']


class CustomProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class CustomUserUpdateForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={

            'placeholder': 'YYYY-MM-DD',

        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input-box',
            'placeholder': 'Enter username'
        })
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input-box',
            'placeholder': 'Enter name'
        })
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'date_of_birth', ]


