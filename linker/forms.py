from django import forms

from .models import LinkModel


class LinkForm(forms.ModelForm):
    class Meta:
        model = LinkModel
        fields = ['name', 'lid', 'target']
        labels = {
            'name': 'Name',
            'lid': 'Link ID',
            'target': 'Target'
        }
