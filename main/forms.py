from django import forms


class CForm(forms.Form):
    image = forms.FileField()
    text = forms.CharField(label='Description')
