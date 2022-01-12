from django import forms
from django.db.models import fields
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome',)