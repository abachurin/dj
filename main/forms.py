from django import forms


class CForm(forms.Form):
    text = forms.CharField()
    image = forms.FileField()
