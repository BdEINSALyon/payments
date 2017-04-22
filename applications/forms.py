from django import forms

from applications.models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('name', 'test_mode')
