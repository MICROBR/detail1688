from django import forms


class InputForm(forms.Form):
    url = forms.URLField(initial='', label='Url')
