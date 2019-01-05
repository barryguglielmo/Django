
from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from .models import Your_CSV

class TheCsvForm (forms.ModelForm):
    class Meta:
        model = Your_CSV
        fields = ['your_csv', 'description']
class GraphForm (forms.ModelForm):
    class Meta:
        model = Your_CSV
        fields = ['description']
