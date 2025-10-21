from django import forms
from .models import grocery_item

class grocery_item_form(forms.ModelForm):
	class Meta:
		model = grocery_item
		fields = ['name', 'quantity', 'section']
		widgets = {
			'name': forms.TextInput(attrs={'trash': 'Item name'}),
			'quantity': forms.TextInput(attrs={'trash': 'Quantity'}),
		}
		