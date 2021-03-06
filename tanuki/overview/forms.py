from django import forms
from django.forms import ModelForm
from .models import AddItem

class DateInput(forms.DateInput):
    input_type = 'date'

class AddItemForm(forms.ModelForm):
    itemName = forms.CharField(
                            label='Item Name', 
                            max_length=100, 
                            widget=forms.TextInput(attrs={'placeholder':'Enter Item Name'})
                            )

    itemPrice = forms.DecimalField(
                                label='Item Price', 
                                max_digits=7, 
                                decimal_places=2,
                                widget=forms.TextInput(attrs={'placeholder': 'Enter Item Price'})
                                )
    
    itemType = forms.CharField(
                            label='Item Type',
                            max_length = 50
                            )

    class Meta:
        model = AddItem
        fields = ('itemName', 'itemPrice', 'itemType', 'dateDisplayed')
        widgets = {
            'dateDisplayed': DateInput()
        }