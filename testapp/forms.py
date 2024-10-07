from django import forms
from .models import Address
from localflavor.us.forms import USStateSelect

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('state', 'city', 'zip_code')
        widgets = {
            'state': USStateSelect,
        }
