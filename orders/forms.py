from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)
    reg_no = forms.CharField(max_length=12)

    class Meta:
        model = User
        fields = ('username','reg_no', 'email', 'password1', 'password2' )