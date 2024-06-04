from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'destination1',
            'destination2',
            'email',
            'names',
            'phone_number',
            'depart_date',
            'return_date',
            'duration'
        ]
        widgets = {
            'depart_date': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input', 'placeholder': 'Depart Date'}),
            'return_date': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input', 'placeholder': 'Return Date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control p-4', 'placeholder': 'Enter your email'}),
            'names': forms.TextInput(attrs={'class': 'form-control p-4', 'placeholder': 'Enter your names'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control p-4', 'placeholder': 'Enter your Phone number'}),
            'duration': forms.Select(attrs={'class': 'custom-select px-4', 'style': 'height: 47px;'})
        }
