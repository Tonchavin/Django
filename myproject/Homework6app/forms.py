import datetime

from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)


class ProductForm(forms.Form):
    id_ = forms.IntegerField()
    name = forms.CharField(max_length=100)
    description = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={'class': "form-control", 'placeholder': 'Product info'}
        ),
    )
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    value = forms.IntegerField()
    date_add = forms.DateField(
        initial=datetime.date.today,
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'type': 'date'}
        ),
    )
    image = forms.ImageField(required=False)
