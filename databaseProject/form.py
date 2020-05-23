from django import forms
from .models import update

class uploadResume(forms.ModelForm):

    class Meta:
        model = update
        fields = "__all__"
