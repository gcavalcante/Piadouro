from django import forms
from piadouro_website.models import Piado


class FormItemPiado(forms.ModelForm):
  class Meta:
    model = Piado
    fields = ['text']

