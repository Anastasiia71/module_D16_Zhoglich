from django import forms
from .models import Ad, Response


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = [
            'author',
            'title',
            'content',
            'category',
        ]


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = [
            'author',
            'text',
            'ad',
        ]
