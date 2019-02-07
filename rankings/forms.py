from django import forms


class AddMatchResult(forms.Form):
    game = forms.CharField(label='Game Name', max_length=160)
