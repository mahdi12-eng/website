from django import forms
from django.forms.widgets import Select


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


class CustomersForm(forms.Form):
    CITY = [
        ('option1', 'Kabul'),
    ]
    STATE = [
        ('option1', 'Chahar-dehi'),
        ('option1', 'Kart-Chahar'),
        ('option1', 'Pule-sorkh'),
        ('option1', 'Darul-Aman'),
    ]
    name = forms.CharField(required=True)
    last_name = forms.CharField(max_length=20, required=True)
    birth_date = forms.DateField(required=True)
    email = forms.EmailField(required=True)

    city = forms.ChoiceField(
        choices=CITY, required=False, widget=Select)
    state = forms.ChoiceField(
        choices=STATE, required=True, widget=Select)
    password = forms.CharField(required=True)
