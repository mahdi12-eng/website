from django import forms
from .models import Customers


class RegisterForm(forms.Form):
    """RegisterForm definition."""

    name = forms.CharField(min_length=4, max_length=50, required=True, widget=forms.TextInput(
        attrs={"class": "form-control rounded-0 border-dark py-3"}),)
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs={"class": "form-control rounded-0 border-dark py-3"}),)
    email = forms.EmailField(min_length=6, max_length=200, required=True, widget=forms.EmailInput(
        attrs={"class": "form-control rounded-0 border-dark py-3"}),)
    DOB = forms.DateField(required=True, widget=forms.DateInput(
        attrs={"class": "form-control rounded-0 border-dark py-3"}),)
    password = forms.CharField(min_length=8, max_length=50, required=True, widget=forms.PasswordInput(
        attrs={"class": "form-control rounded-0 border-dark py-3"}),)


class LoginForm(forms.Form):
    """LoginForm definition."""

    email = forms.EmailField(min_length=6, max_length=200, required=True, widget=forms.EmailInput(
        attrs={"class": "form-control rounded-0 border-dark py-3"}),)
    password = forms.CharField(min_length=8, max_length=50, required=True, widget=forms.PasswordInput(
        attrs={"class": "form-control rounded-0 border-dark py-3"}),)


class CustomersForm(forms.ModelForm):

    class Meta:
        model = Customers
        fields = "__all__"

        # ['cs_name', 'cs_lastname',
        #           'email', 'birth_date', 'password',]
