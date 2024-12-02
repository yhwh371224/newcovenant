from django import forms
from .models import Bulletin


class BulletinForm(forms.ModelForm):
    class Meta:
        model = Bulletin
        fields = ['title', 'date', 'pdf_file']
