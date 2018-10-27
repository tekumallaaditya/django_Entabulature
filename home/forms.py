from django import forms
from .models import testimonialDB

class testimonialForm(forms.ModelForm):
    name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name...'
        }
        ))

    testimonial = forms.CharField( widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your comments...'
        }
    ) )


    class Meta:
        model = testimonialDB
        fields = ('name', 'testimonial')