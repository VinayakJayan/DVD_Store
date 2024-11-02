from django import forms
from .models import Booking
class DateInput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        labels={
            'cs_name':"Customer Name",
            'cs_phno':"Customer Number:",
            'name':"Movie Name:",
            
        }

