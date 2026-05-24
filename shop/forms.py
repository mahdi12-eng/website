from django import forms
from .models import Customers


class RegisterForm(forms.Form):
    """RegisterForm definition."""

    name = forms.CharField(min_length=4, max_length=50, required=True,)
    last_name = forms.CharField(max_length=50, required=True, )
    email = forms.EmailField(min_length=6, max_length=200, required=True,)
    DOB = forms.DateField(required=True,)
    password = forms.CharField(min_length=8, max_length=50, required=True,)


class LoginForm(forms.Form):
    """LoginForm definition."""

    email = forms.EmailField(min_length=6, max_length=200, required=True)
    password = forms.CharField(min_length=8, max_length=50, required=True)


class CustomersForm(forms.ModelForm):

    class Meta:
        model = Customers
        fields = "__all__"

        # ['cs_name', 'cs_lastname',
        #           'email', 'birth_date', 'password',]
