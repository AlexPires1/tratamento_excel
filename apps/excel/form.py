from django import forms
from .models import *


class ExcelForm(forms.ModelForm):

    class Meta:
        model = Excel
        fields = 'excel',

    def __init__(self, *args, **kwargs):
        super(ExcelForm, self).__init__(*args, **kwargs)
