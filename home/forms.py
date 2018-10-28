from django import forms
from .models import testimonialDB, contactUsDB

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

class contactUsForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'enter your name here...'
        }
    ))
    sender = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'enter your email here...'
        }
    ))
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'enter your message here...'
        }
    ))

    class Meta:
        model = contactUsDB
        fields = ('name', 'sender', 'message')