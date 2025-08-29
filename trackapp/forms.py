from django import forms
#from django.forms.fields import UUIDField

class TrackingForm(forms.Form):
    tracking_id = forms.UUIDField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter your tracking code (e.g. 550e8400-e29b-41d4-a716-446655440000)',
                'style': 'width:100%'
            }
        )
    )