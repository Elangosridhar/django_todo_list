from django import forms

class PositionForm(forms.Form):
    position = forms.CharField()

class PositionFor(forms.Form):
    position = forms.CharField()