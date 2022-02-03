from django import forms

from web_admin.models import New


class NewCreateForm(forms.ModelForm):
    class Meta:
        model = New
        fields = '__all__'